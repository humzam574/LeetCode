class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        #basically a buffed two sum
        ban = set(banned)
        curr = 0
        ans = 0
        for i in range(1, n+1):
            if i not in ban:
                curr+=i
                if curr > maxSum:
                    return ans
                ans+=1
        return ans


