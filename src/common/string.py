class String(str):
    def is_palindrome(self) -> bool:
        limit: int = len(self) // 2

        for i in range(limit):
            if self[i] != self[len(self) - i - 1]:
                return False
        return True
