class Problem2:
    term0 = 0
    term1 = 1

    @staticmethod
    def solve(limit):
        num_sum = 0
        a = Problem2.term0
        b = Problem2.term1

        while a + b < limit:
            c = a + b
            a = b
            b = c

            if c % 2 == 0:
                num_sum += c

        return num_sum
