import flask

app = flask.Flask("convurs")

message_list = ['Hello!']

@app.route('/')
def hello():
    message = flask.request.args.get('message')
    if message is not None:
        message_list.append(message)
    return message_list[-1]

if __name__ == '__main__':
    app.run(debug=True)
