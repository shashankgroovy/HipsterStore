# Put all your views here.
from HipsterStore import app
from flask import render_template

@app.route('/')
def landingPage():
    return render_template('landingPage.html')

