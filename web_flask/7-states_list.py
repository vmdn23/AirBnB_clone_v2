#!/usr/bin/python3
"""
Render HTML for List of states using jinja and flask
"""


from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_html():
    """
    Display states from storage
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    close storage
    """
    storage.close()


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
