class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        ans, stack, nums = [0]*len(nums), [-1], nums + [100001]
        for i,n in enumerate(nums):
            while nums[stack[-1]] < n: ans[stack.pop()] = i-stack[-2]-1
            stack.append(i)
        return ans