from main import hello

def test_always_true():
    assert True == True

def test_hello():
    assert hello() == "Hello World"