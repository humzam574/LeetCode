class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stacc, ans = [(nums[0], 0)], 0
        for i,num in enumerate(nums[1:]):
            if stacc[-1][0] > num:
                stacc.append((num,i+1))
        for i in range(len(nums) - 1, 0, -1):
            while stacc and nums[i] >= stacc[-1][0]:
                ans = max(ans, i - stacc[-1][-1])
                stacc.pop()
            #if not stacc: break
        return ans