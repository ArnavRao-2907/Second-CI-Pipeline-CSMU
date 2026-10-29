from codes.Most_Frequent_36 import mf

def test_a():
    assert mf([1,3,5,2, 0, 1, 5, 5]) == 5

def test_b():
    assert mf([]) == None

def test_c():
    assert mf([0]) == 0

def test_d():
    assert mf([8, 8]) == 8

def test_e():
    assert mf([1, 3]) == 1
