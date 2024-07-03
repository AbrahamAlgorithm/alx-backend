#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index page with a welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
