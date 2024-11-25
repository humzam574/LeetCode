class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
        m= [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wd:
                start = i - len(w)
                if start >= 0 and m[start] and s[start:i] == w:
                    m[i] = True
                    break
        
        return m[-1]