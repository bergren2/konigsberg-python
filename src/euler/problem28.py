class Problem28:
    def __init__(self, size: int):
        self.size = size

    def solve(self):
        sum: int = 0

        for i in range(1, self.size + 1, 2):
            sum += Problem28.diag_ring_sum(i)

        return sum

    @staticmethod
    def diag_ring_sum(size: int) -> int:
        if size == 1:
            return 1 # special case, there's only one instead of four
        else:
            # m stands for magic number
            # aka the middle left number in a given ring for the size
            m: int = ((size - 1) ** 2) + 1 + (size // 2)
            return 4 * m