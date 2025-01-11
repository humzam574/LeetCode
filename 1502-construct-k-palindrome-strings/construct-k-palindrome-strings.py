class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dict = Counter(s)
        if k > len(s): return False
        odds = 0
        for g, v in dict.items():
            odds += (v % 2)
        return odds <= k