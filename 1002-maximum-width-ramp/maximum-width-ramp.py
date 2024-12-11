class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack, ans = [0], 0
        for i in range(1, len(nums)): stack.append(i) if nums[stack[-1]] > nums[i] else None
        for i in range(len(nums) - 1, 0, -1):
            while stack and nums[i] >= nums[stack[-1]]: ans = max(ans, i - stack[-1]); stack.pop()
        return ans