import flask

app = flask.Flask("convurs")

def load_messages():
    with open('messages.txt') as f:
        return [message.strip() for message in f.readlines()]

def save_messages(message_list):
    with open('messages.txt', 'w') as f:
        for message in message_list:
            f.write(message.strip() + '\n')

@app.route('/')
def chat():
    message_list = load_messages()

    message = flask.request.args.get('message')
    if message is not None and message.strip() != '':
        message_list.append(message)

    save_messages(message_list)

    return flask.render_template("chat.html", message_list=message_list)

if __name__ == '__main__':
    app.run(debug=True)
