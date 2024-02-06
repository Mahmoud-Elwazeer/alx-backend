#!/usr/bin/env python3
"""import libraries"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """setting Babel’s default locale ("en") and timezone ("UTC")."""
    LANGUAGES = ['en', 'fr']

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# def get_locale():
#     """ determine the best match with our supported languages."""
#     return request.accept_languages.best_match(app.config['LANGUAGES'])
# babel = Babel(app, default_locale=get_locale)

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.default_locale
def get_locale():
    """ determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def home():
    """render home page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
