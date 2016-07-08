import flask

app = flask.Flask("convurs")

@app.route('/')
def hello():
    return 'Hello!'

if __name__ == '__main__':
    app.run(debug=True)
