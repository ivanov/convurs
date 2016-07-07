import flask

app = flask.Flask("supersnarq")

@app.route('/')
def snarqy_frontpage():
    return "hello world"

@app.route('/say/<msg>')
@app.route('/say')
def send_hello(msg='Cat got your tongue?'):
    return msg

if __name__ == '__main__':
    app.run()
