import flask

app = flask.Flask("convurs")

@app.route('/')
def chat():
    return flask.render_template("logo.html")

if __name__ == '__main__':
    app.run(debug=True)
