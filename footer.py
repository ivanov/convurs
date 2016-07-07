import flask

app = flask.Flask("supersnarq")

footer = """
<div>
this always appears as the last thing on our page
</div>
"""

@app.route('/')
def convurs_frontpage():
    return "hello world"

@app.route('/say/<msg>')
def send_hello(msg):
    return msg + footer

if __name__ == '__main__':
    app.run()


# here we grab a portion of the URL and pass it as a parameter to a function
#
# demo html tags http://localhost:5000/say/yo%3Cbr%3E%3Cb%3Esup
