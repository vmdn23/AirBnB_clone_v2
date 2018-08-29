#!/usr/bin/python3
"""
Render HTML for cities by states using jinja and flask
"""


from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    close storage
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """
    Display states from storage
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display an html page city by state
    """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
def state_and_state():
    """
    Display an html page with state and state.id
    """
    states_all = storage.all("State")
    return render_template('9-states.html', states_all=states_all)


@app.route('/states/<path:id>', strict_slashes=False)
def state_id(id):
    """
    Display an html page if id is found
    """
    state_list = storage.all("State")
    states = []

    for state in state_list.values():
        if state.id == id:
            states.append(state)

    return render_template('9-states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
