from bank import value

def test_value():
    assert value("здравствуйте") == "$0"
    assert value("здрасти") == "$20"
    assert value("прив") == "$100"