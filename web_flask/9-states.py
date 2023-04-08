#!/usr/bin/python3
"""Initialize a Flask application with state_list, using the Storage"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>")
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for states in storage.all("State").values():
        if states.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)