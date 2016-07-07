from snarq import app

app.testing = True

def test_homepage():
    with app.test_client() as c:
        rv = c.get('/')
        assert 'hello world' in  rv.data  # deliberate typo here
        #assert 'hellow world' in  rv.data  # deliberate typo here

def test_say():
    with app.test_client() as c:
        rv = c.get('/say/this is awesome')
        assert 'this is awesome' in  rv.data

def test_say_without_argument():
    with app.test_client() as c:
        rv = c.get('/say')
        print rv.data
        assert 'Cat got your tongue?' in  rv.data

# 08.py
