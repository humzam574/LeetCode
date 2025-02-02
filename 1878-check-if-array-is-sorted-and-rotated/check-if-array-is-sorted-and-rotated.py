class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            nums = nums[1:] + [nums[0]]
            if sorted(nums) == nums:
                return True
        return False