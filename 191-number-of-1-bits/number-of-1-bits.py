class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        b=str(b)
        return b.count('1')