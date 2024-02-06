#!/usr/bin/env python3
"""import libraries"""

from flask import Flask, template_rendered

app = Flask(__name__)


@app.route("/")
def home():
    """render home page"""
    return template_rendered('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)