from codes.Check_Sorted_34 import cs
cs([1, 10])
def test_a():
    assert cs([1, 10]) == True

def test_b():
    assert cs([9, 10, 0]) == False

def test_c():
    assert cs([9, 9]) == True

def test_d():
    assert cs([]) == None

def test_e():
    assert cs([9, 10, ]) == True