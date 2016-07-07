import flask

app = flask.Flask("convurs")

@app.route('/')
def convurs_frontpage():
    return "hello world"

if __name__ == '__main__':
    app.run()


# this is just a pythonism - if we want to reuse parts of convurs elsewhere (in
# our testing code, for example,
#
# allows us to `import convurs` or `from convurs import app`,
# let's write a basic test test_06.py
#
# show python convurs.py vs python and import convurs at the command line
#
# git commit
#
# write that test test_06.py
