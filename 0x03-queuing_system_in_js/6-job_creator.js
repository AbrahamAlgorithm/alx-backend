import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '4153518780',
    message: 'This is a test message'
}

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log('Notification job failed to create');
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});