from konigsberg.euler.problem2 import Problem2


def test_sample():
    problem = Problem2()
    assert problem.solve(10) == 10
    assert problem.solve(90) == 44


def test_actual():
    problem = Problem2()
    assert problem.solve(4000000) == 4613732
