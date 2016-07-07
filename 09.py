import flask

app = flask.Flask("supersnarq")

storage = []  # an empty list

@app.route('/')
def snarqy_frontpage():
    return "hello world"

@app.route('/say/<msg>')
@app.route('/say')
def send_hello(msg='Cat got your tongue?'):
    storage.append(msg)
    return "<br>".join(storage)

if __name__ == '__main__':
    app.run()

# test_09
#
# yay, tests pass!
#
# let's go deploy this?
#
#
# pip freeze > requirements.txt
#
# git commit that!
