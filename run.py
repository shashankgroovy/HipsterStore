# This is the runserver file and should be used to run the app.
# While using on a production server make sure the DEBUG flag is set to False.

# Add the following to your webserver
# web: gunicorn run:app

from HipsterStore import app
app.run()
