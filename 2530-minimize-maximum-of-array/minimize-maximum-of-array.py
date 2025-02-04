class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr = ans = 0
        for i in range(len(nums)):
            curr += nums[i]
            ans = max(ans, curr // (i+1) + (curr % (i+1) != 0))
        return int(ans)
