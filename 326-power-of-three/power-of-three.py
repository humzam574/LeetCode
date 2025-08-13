class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(20):
            if n == int(3**i):
                return True
        return False