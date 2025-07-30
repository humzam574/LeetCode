class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        prev = 0
        for t in target:
            if t > prev:
                ans += t - prev
            prev = t
        return ans