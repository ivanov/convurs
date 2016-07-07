import flask

app = flask.Flask("convurs")

message_list = []

@app.route('/')
def chat():
    name = flask.request.args.get('name')
    if name is None or name == '':
        name = 'Anonymous'
    message = flask.request.args.get('message')
    if message is not None:
        message_list.append((name, message))
    return flask.render_template("chat_names.html", message_list=message_list)


if __name__ == '__main__':
    app.run(debug=True)
