import math


class Problem3:
    def __init__(self):
        pass

    def solve(self, n: int) -> int:
        limit: int = math.floor(math.sqrt(n))
        prime_factors: list[int] = []

        for i in range(2, limit):
            if n % i == 0:
                is_prime: bool = True  # default

                for p in prime_factors:
                    if i % p == 0:
                        is_prime = False  # found a smaller divisor
                        break

                if is_prime:
                    prime_factors.append(i)

        return prime_factors[-1]
