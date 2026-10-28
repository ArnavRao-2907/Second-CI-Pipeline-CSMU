from codes.Move_Zeroes_35 import mz

def test_a():
    assert mz([1,2,4,5,3,0,8,0,80], 9) == [1, 2, 4, 5, 3, 8, 80, 0, 0]
    
def test_b():
    assert mz([0, 1, 0, 8], 4) == [1, 8 ,0, 0]
    
def test_c():
    assert mz([], 0) == []
    
def test_d():
    assert mz([2, 9, 8, ], 3) == [2, 9, 8]
    
def test_e():
    assert mz([0], 1) == [0]
