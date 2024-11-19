from pythoncalculator import divide


def test_divide():
    assert divide(10, 2) == 5
    assert divide(30, 2) == 15
    assert divide(10, 5) == 2
