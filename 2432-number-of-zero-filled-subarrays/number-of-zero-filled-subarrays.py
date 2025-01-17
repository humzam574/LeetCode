class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        #n -> (n^2+n)/2
        l = 0
        ans = 0
        while l < len(nums):
            if nums[l] == 0:
                temp = l
                while temp < len(nums) and nums[temp] == 0:
                    temp += 1
                val = temp - l
                ans += (val*val + val)//2
                l = temp
            l += 1
        return ans