from convurs import app

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

# 07.py
