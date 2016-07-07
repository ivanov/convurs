import flask

app = flask.Flask("supersnarq")

@app.route('/')
def snarqy_frontpage():
    return "hello world"

if __name__ == '__main__':
    app.run()


# this is just a pythonism - if we want to reuse parts of snarq elsewhere (in
# our testing code, for example,
#
# allows us to `import snarq` or `from snarq import app`,
# let's write a basic test test_06.py
#
# show python snarq.py vs python and import snarq at the command line
# 
# git commit
#
# write that test test_06.py
