class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d = []
        curr = []
        if s1 == s2: return True
        for i, char in enumerate(s2):
            if s2[i] != s1[i]:
                d.append(s2[i])
                curr.append(s1[i])
        return len(d) == 2 and curr[::-1] == d