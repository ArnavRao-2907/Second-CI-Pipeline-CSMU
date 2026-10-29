from codes.Rotate_String_37 import rs

def test_a():
    assert rs("abcdef", 2) == "cdefab"

def test_b():
    assert rs(" ", 8) == " "

def test_c():
    assert rs("8089", 9) == "0898"

def test_d():
    assert rs("@rnAv", 3) == "Av@rn"

def test_e():
    assert rs("abc", 1) == "bca"
