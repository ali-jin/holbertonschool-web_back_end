#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def hello_world():
    """ Render HTML """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
