import flask

app = flask.Flask("supersnarq")

@app.route('/')
def convurs_frontpage():
    return "hello world"

@app.route('/say/<msg>')
def send_hello(msg):
    return msg

if __name__ == '__main__':
    app.run()


# here we grab a portion of the URL and pass it as a parameter to a function
#
# demo html tags http://localhost:5000/say/yo%3Cbr%3E%3Cb%3Esup
#
#
#  test_07.py
#
#  tests pass? git commit!
#
#
# ok, what about visiting just /say
#
#  Not Found  The requested URL was not found on the server.  If
#  you entered the URL manually please check your spelling and
#  try again.
#
#
# test_08.py
