import os
from flask import Flask


# create our awesome application
app = Flask(__name__)
app.config.from_object(__name__)

# TODO: figure out how to import configs
#app.config.from_pyfile('config.py')

# set the environment variable on your Linux
# $ export FLASKR_SETTINGS = /path/to/settings.cfg
app.config.from_envvar('HIPSTER_SETTINGS', silent=True)

# Get the views
# To avoid 'Circular Imports' b/w __init__.py and views.py,
# the views have been imported at the end of file.
import HipsterStore.views

if __name__=='__main__':
    app.run()
