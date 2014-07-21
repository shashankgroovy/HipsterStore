import os
from flask import Flask


# create are awesome application
app = Flask(__name__)
app.config.from_object(__name__)
#app.config.from_pyfile('config.py')

# set the environment variable on your Linux
# $ export FLASKR_SETTINGS = /path/to/settings.cfg
app.config.from_envvar('HIPSTER_SETTINGS', silent=True)

# Get the views
import HipsterStore.views

if __name__=='__main__':
    app.run()
