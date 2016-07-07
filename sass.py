import flask

app = flask.Flask("convurs")

@app.route('/')
def convurs_frontpage():
    return "hello world"

@app.route('/say/<msg>')
@app.route('/say')
def send_hello(msg='Cat got your tongue?'):
    return msg

if __name__ == '__main__':
    app.run()
