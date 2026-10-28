from codes.Count_Words_32 import cw

def test_a():
    assert cw("12 45678") == 8
    
def test_b():
    assert cw("") == 0
    
def test_c():
    assert cw(" ") == 1
    
def test_d():
    assert cw("Abcd ^7=. ") == 10
    
def test_e():
    assert cw(" None ") == 6