#!/usr/bin/python3
"""Script that starts a Flask web app that listens on 0.0.0.0, port 5000"""


from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text="is cool"):
    """Display Python , followed by the value of the text variable"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """Display n is a number only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer and
    H1 tag: Number: n, inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """Display a HTML page only if n is an integer and
    H1 tag: Number: n is even|odd inside the tag BODY
    """
    if n % 2 == 1:
        number = '{} is odd'.format(n)
    else:
        number = '{} is even'.format(n)
    return render_template('6-number_odd_or_even.html', n=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
