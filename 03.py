# before - talk about the abundance of python frameworks
# - bottle
# - flask
# - cherrypy
# - django (we use here)
# - pyramid
# - web.py
#
#
# We're going to use Flask - mkvirtualenv snarq-env
#
# workon snarq
#
# pip install flask

import flask

app = flask.Flask("supersnarq")

@app.route('/')
def convurs_frontpage():
    print "hello world"

convurs_frontpage()

# maybe put a  <strong> </strong> around world?
