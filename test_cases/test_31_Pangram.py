from codes.Pangram_31 import isp

def test_a():
    assert isp("The quick brown fox jumps over the lazy dog") == True
    
def test_b():
    assert isp("Hello World") == False
    
def test_c():
    assert isp("AbcdeFghiJklmnoPQRstu8vw345xyz") == True
    
def test_d():
    assert isp("0(1)") == False
    
def test_e():
    assert isp("") == False