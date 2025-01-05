class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        tot = sum((1 if direct == 1 else -1) * amt for direct, amt in shift)
        for i in range(tot % len(s)): s = s[1:] + s[0] if (tot % len(s)) < 0 else s[-1] + s[:-1]
        return s