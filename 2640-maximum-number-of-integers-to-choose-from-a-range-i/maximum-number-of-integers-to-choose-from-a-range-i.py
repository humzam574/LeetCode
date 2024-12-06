class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban, ans = set(banned), 0
        for i in range(1, n+1):
            if i not in ban:
                maxSum, ans = maxSum - i, ans + 1
                if maxSum < 0: return ans-1
        return ans