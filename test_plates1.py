from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("CS50")==True
    assert is_valid("C50")==False
    assert is_valid("50CS")==False
    assert is_valid("50")==False
def test_length():
    assert is_valid("CS")==True
    assert is_valid("CS50000")==False
    assert is_valid("C")==False
def test_numbers_placement():
    assert is_valid("AAA22A")==False
    assert is_valid("CS05")==False
    assert is_valid("CS50")==True
def test_punctuation():
    assert is_valid("PI3.14")==False
    assert is_valid("CS 50")==False
    assert is_valid("CS50!")==False

