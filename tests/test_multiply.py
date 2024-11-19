from pythoncalculator import multiply


def test_multiply():
    assert multiply(10, 3) == 30
    assert multiply(5, 3) == 15
    assert multiply(6, 5) == 30