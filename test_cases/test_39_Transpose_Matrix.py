from codes.Transpose_Matrix_39 import tm

def test_a():
    mat = [[1, 2, 3],[4, 5, 6]]
    assert tm(mat) == [[1, 4], [2, 5], [3, 6]]

def test_b():
    mat = [[1, 2], [4, 5], [7, 8]]
    assert tm(mat) == [[1, 4, 7], [2, 5, 8]]

def test_c():
    mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert tm(mat) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def test_d():
    mat = [[1]]
    assert tm(mat) == [[1]]

def test_e():
    mat = [ ]
    assert tm(mat) == []
