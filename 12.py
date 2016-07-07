import flask

app = flask.Flask("convurs")

storage = []  # an empty list

@app.route('/')
def convurs_frontpage():
    return "hello world"

@app.route('/say/<msg>')
@app.route('/say')
def say_message(msg='Cat got your tongue?'):
    attributed_msg = "<div><b>" + "anonyMouse" + "</b>: " + msg + "</div>"
    storage.append(attributed_msg)
    return "".join(storage)

@app.route('/login/<username>/<msg>')
@app.route('/login/<username>')
def user_say(username, msg='Cat got your tongue?'):
    attributed_msg = "<div><b>" + username + "</b>: " + msg + "</div>"
    storage.append(attributed_msg)
    return "".join(storage)

if __name__ == '__main__':
    app.run()


# now let's add some "users"
