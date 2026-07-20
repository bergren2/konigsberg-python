from common.fibseq import FibSeq

class Problem2:
    def __init__(self):
        self.term0 = 0
        self.term1 = 1


    def solve(self, limit: int) -> int:
        fib = FibSeq(self.term0, self.term1)
        return fib.sum_of_terms(limit, Problem2.is_even)

    @staticmethod
    def is_even(num: int) -> bool:
        return num % 2 == 0