const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const port = 1245;

// Redis client setup
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize seats and reservation flag
const initialSeats = 50;
let reservationEnabled = true;

// Kue queue setup
const queue = kue.createQueue();

// Function to set the number of available seats
async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

// Function to get the current number of available seats
async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return seats ? parseInt(seats, 10) : 0;
}

// Set initial number of available seats
reserveSeat(initialSeats);

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save(err => {
        if (err) {
            return res.json({ status: 'Reservation failed' });
        }
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
    });
});

// Route to process the queue
app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const seats = await getCurrentAvailableSeats();
        if (seats <= 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }

        await reserveSeat(seats - 1);
        if (seats - 1 === 0) {
            reservationEnabled = false;
        }

        done();
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
