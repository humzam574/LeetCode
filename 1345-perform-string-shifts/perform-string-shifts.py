class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        return (lambda i: s[i:] + s[:i])(sum(x * (1-2*d) for d, x in shift) % len(s))