# got this code from flask documentation

from convurs import app

app.testing = True

def test_homepage():
    with app.test_client() as c:
        rv = c.get('/')
        assert 'hello world' in  rv.data  # deliberate typo here
        #assert 'hellow world' in  rv.data  # deliberate typo here

test_homepage()


# make test pass
# but actually - let's use a tool that'll run the test suite for us
#
# pip install nosetests
#
# $ nosetests .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# OK
#
# great, let's write another test for functionality we haven't written yet
#
# test_07.py
#
