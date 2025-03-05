class Solution:
    def coloredCells(self, n: int) -> int:
        #1, 5, 13, 25, 41
        #1, 4, 8, 12, 16
        curr = 1
        delta = 4
        for i in range(n - 1):
            curr += delta
            delta += 4
        return curr