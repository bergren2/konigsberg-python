from euler.problem36 import Problem36


def test_sample():
    problem = Problem36()
    assert problem.solve(0) == 0
    assert problem.solve(1) == 0
    assert problem.solve(2) == 1
    assert problem.solve(3) == 1
    assert problem.solve(6) == 9


def test_actual():
    problem = Problem36()
    assert problem.solve(1_000_000) == 872187
