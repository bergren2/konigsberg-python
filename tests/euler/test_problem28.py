from euler.problem28 import Problem28

def test_sample():
    assert Problem28(5).solve() == 101

def test_actual():
    assert Problem28(1001).solve() == 669171001
