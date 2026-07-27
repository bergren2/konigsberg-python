from common.string import String


def test_true():
    s = String("racecar")
    assert s.is_palindrome()

def test_false():
    s = String("butterfly")
    assert not s.is_palindrome()

def test_long_true():
    s = String("saippuakivikauppias") # Finnish for "soapstone vendor"
    assert s.is_palindrome()

def test_long_false():
    s = String("racecars aren't racecar")
    assert not s.is_palindrome()