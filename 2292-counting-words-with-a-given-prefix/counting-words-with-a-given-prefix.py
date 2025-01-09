class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int: return sum(words[i].startswith(pref) for i in range(len(words)))