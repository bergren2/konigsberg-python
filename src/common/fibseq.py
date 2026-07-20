from collections.abc import Callable

class FibSeq:
    def __init__(self, term0: int, term1: int):
        self.term0 = term0
        self.term1 = term1


    @staticmethod
    def constant_true(_):
        return true


    def sum_of_terms(self, limit: int, condition: Callable[[int], bool] = constant_true):
        num_sum = 0
        a = self.term0
        b = self.term1

        while a + b < limit:
            c = a + b
            a = b
            b = c

            if condition(c):
                num_sum += c

        return num_sum