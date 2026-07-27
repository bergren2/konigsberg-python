from euler.problem3 import Problem3


def test_sample():
    problem = Problem3()
    assert problem.solve(13195) == 29


def test_actual():
    problem = Problem3()
    assert problem.solve(600851475143) == 6857
