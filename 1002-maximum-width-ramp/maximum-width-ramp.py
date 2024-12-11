class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        #use monotonic stacc
        #create a stack and as you start iterating add numbers which are strictly decreasing
        stacc = [(nums[0], 0)]
        for i,num in enumerate(nums[1:]):
            if stacc[-1][0] > num:
                stacc.append((num,i+1))
        #print(stacc)
        ans = 0
        for i in range(len(nums) - 1, 0, -1):
            while stacc and nums[i] >= stacc[-1][0]:
                ans = max(ans, i - stacc[-1][-1])
                stacc.pop()
            if not stacc:
                return ans
            
        return ans