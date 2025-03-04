class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while (n != 0):
            if (1 + sum(int(c) for c in str(n))) % 3 == 0:
                return False
            n = n // 3
        return True