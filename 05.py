import flask

app = flask.Flask("supersnarq")

@app.route('/')
def convurs_frontpage():
    return "hello world"

app.run()


# HUZZAH! it works
#
# git diff before committing - to see what's changed
#
#
# then git commit it!
#
#
#
# here's what we're using from flask so far:
# mapping urls to python functions which return strings that get rendered as
# pages in the browser
