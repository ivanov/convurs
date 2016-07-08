import flask

app = flask.Flask("convurs")

@app.route('/')
def hello():
    return 'Hello GirlsWhoCode!'

if __name__ == '__main__':
    app.run(debug=True)
