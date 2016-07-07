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
        assert 'Cat got your tongue?' in  rv.data

def test_say_persits():
    with app.test_client() as c:
        rv = c.get('/say/this is awesome')
        assert 'this is awesome' in  rv.data
        rv = c.get('/say/but not earth shattering')
        assert 'this is awesome' in  rv.data
        assert 'earth shattering' in  rv.data

# 09.py
