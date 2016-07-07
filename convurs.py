import flask

app = flask.Flask("convurs")

message_list = []

@app.route('/')
def chat():
    message = flask.request.args.get('message')
    if message is not None:
        message_list.append(message)
    return flask.render_template("chat.html", message_list=message_list)

if __name__ == '__main__':
    app.run()
