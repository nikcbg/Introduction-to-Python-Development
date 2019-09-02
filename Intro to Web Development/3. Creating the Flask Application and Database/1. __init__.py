'''
There are a few things to note here:

1. We're naming our Flask application based on the __name__ value which will correspond to the FLASK_APP environment variable.
2. Our function can receive an optional test_config object so that it can be configured differently if we ever decide to write automated tests.
3. The app.config.from_mapping call allows us to set configuration constants. We need to have a SECRET_KEY and we're setting that now, but should load a specific value from the environment when this application is deployed.
4. The final thing that we need to do is return the application from the function so that the Flask CLI can run it.

To run our application, we'll use the flask CLI after setting a few environment variables:

(notes) $ export FLASK_ENV=development
(notes) $ export FLASK_APP='.'
(notes) $ flask run --host=0.0.0.0 --port=3000
 * Serving Flask app "." (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 143-698-723
The flask CLI will automatically reload code for us as we're developing, and serve our application on port 3000. We'll want to leave this running, so let's connect to the workstation again in a separate terminal tab. We can currently see our empty Flask app by going to our server's public IP address on port 3000.

We should receive a "Not Found" but that's fine. We haven't defined any routes yet, so there are no resources to find.
'''

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    return app
