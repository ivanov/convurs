# pull up flask docs / webpage
import flask

app = flask.Flask("convurs")

@app.route('/')
def convurs_frontpage():
    print "hello world"

app.run()


# git commit - so we can always come back here

#omg - Internal Server Error? our first crash!
#   - well, sort of  - server is still running
#   - ... let's go look at the flask hello world to see what might be going on
#
#   http://flask.pocoo.org/docs/0.10/quickstart/
