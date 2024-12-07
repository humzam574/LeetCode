class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        val = max(nums)
        ans = 0
        for i in range(k):
            ans+=val
            val+=1
        return ans