#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """Displays C followed by the value of the text variable"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run()
