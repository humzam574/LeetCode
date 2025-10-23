class Solution:
    def hasSameDigits(self, s: str) -> bool:
        stacc = []
        while len(s) > 2:
            stacc = []
            for i in range(len(s)-1):
                n = int(s[i])
                stacc.append((int(s[i]) + int(s[i+1]))%10)
            s = ''.join([str(c) for c in stacc])
        return s[0] == s[-1]
