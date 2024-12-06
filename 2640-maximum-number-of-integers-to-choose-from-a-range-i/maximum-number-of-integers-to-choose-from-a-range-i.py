class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban, curr, ans = set(banned), 0, 0
        for i in range(1, n+1):
            if i not in ban:
                curr, ans = curr + i, ans + 1
                if curr > maxSum: return ans-1
        return ans