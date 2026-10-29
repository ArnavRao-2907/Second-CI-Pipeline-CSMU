from codes.Gcd_40 import ans

def test_a():
    assert ans(12, 14) == 2
    
def test_b():
    assert ans(9, 9) == 9
    
def test_c():
    assert ans(9, 0) == 9
    
def test_d():
    assert ans(2, 128) == 2
    
def test_e():
    assert ans(2, 127) == 1