from collections.abc import Iterator

from common.string import String


class Problem36:
    def __init__(self):
        pass

    def solve(self, limit):
        return sum(Problem36.pali_check(limit))

    @staticmethod
    def pali_check(limit: int) -> Iterator[int]:
        for i in range(1, limit):
            base10 = String(i)
            base2 = String(bin(i)[2:])
            if base10.is_palindrome() and base2.is_palindrome():
                yield i