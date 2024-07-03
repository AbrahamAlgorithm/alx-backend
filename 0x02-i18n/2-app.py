#!/usr/bin/env python3
"""
This module sets up a basic
Flask application with i18n support using Flask-Babel.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

class config:
    """
    This class configures the application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    
app = Flask(__name__)
app.config.from_object(config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determine the user's locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Render the index page with a welcome message
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run()