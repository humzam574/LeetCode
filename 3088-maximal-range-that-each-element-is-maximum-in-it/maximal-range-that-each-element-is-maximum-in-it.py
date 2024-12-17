class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        nums.append(inf)
        stack = [-1]
        for i,n in enumerate(nums):
            while nums[stack[-1]] < n:
                ans[stack.pop()] = i-stack[-2]-1
            stack.append(i)
        return ans