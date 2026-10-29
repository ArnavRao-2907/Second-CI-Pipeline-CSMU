from codes.Missing_Number_Xor_38 import mnx
print(mnx([1,2,4,5], 5))
3
def test_a():
    assert mnx([1,2,4,5], 5) == 3
    
def test_b():
    assert mnx([], 0) == 0

def test_c():
    assert mnx([1, 3, ], 3) == 2

def test_d():
    assert mnx([19], 1 ) == 18

def test_e():
    assert mnx([19], 0) == 19
