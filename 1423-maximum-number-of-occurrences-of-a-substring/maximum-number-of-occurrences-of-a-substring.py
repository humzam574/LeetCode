class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dict = defaultdict(int)
        for r in range(minSize, len(s) + 1):
            if len(set(s[r-minSize:r])) <= maxLetters:
                dict[s[r-minSize:r]]+=1
        if not dict: return 0
        val = max(dict.values())
        return val