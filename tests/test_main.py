from app.main import add

def test_add():
    assert add(23, 5) == 28

def test_deliberately_broken():
    assert 1 == 2, "this should fail on purpose"
