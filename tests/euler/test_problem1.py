from euler.problem1 import Problem1


def test_sample():
    problem = Problem1()
    assert problem.solve(10) == 23


def test_actual():
    problem = Problem1()
    assert problem.solve(1000) == 233168
