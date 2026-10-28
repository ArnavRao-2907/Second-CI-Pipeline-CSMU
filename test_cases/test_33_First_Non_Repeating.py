from codes.First_Non_Repeating_33 import fnr

def test_a():
    assert fnr("swiss") == 'w'

def test_b():
    assert fnr("") == None

def test_c():
    assert fnr(" ") == ' '

def test_d():
    assert fnr("4tt65") == '4'

def test_e():
    assert fnr("-+-98*") == '+'
