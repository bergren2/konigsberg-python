class Problem1:
    @staticmethod
    def solve(limit):
        num_sum = 0
        for i in range(1, limit):
            if i % 3 == 0 or i % 5 == 0:
                num_sum += i

        return num_sum
