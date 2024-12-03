class Solution:
    def addSpaces(self, s: str, p: List[int]) -> str: return " ".join(s[l:i] for l, i in zip([0] + p, p + [len(s)]))