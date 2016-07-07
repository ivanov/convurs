# before - talk about the abundance of python frameworks
# - bottle
# - flask
# - cherrypy
# - django (we use here)
# - pyramid
# - web.py
#
#
# We're going to use Flask - mkvirtualenv convurs-env
#
# workon convurs
#
# pip install flask

import flask

app = flask.Flask("convurs")

@app.route('/')
def convurs_frontpage():
    print "hello world"

convurs_frontpage()

# maybe put a  <strong> </strong> around world?
