#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0, port 5000
"""
from flask import *
from models import storage

app = Flask(__name__)


# @app.route('/states_list/<value>', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """Displays a HTML page with the list of all State objects"""
    states = storage.all('State')
    # states = sorted(states, key=lambda x x.name)
    # states= sort(attribute='state.name')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
