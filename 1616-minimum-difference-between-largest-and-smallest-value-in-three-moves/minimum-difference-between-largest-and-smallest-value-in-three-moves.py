class Solution:
    def minDifference(self, n: List[int]) -> int: n.sort(); return 0 if len(n) < 5 else min(n[-1] - n[3], n[-2] - n[2], n[-3] - n[1], n[-4] - n[0])

        
