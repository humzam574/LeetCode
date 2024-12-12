class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = {nums[0]: 0}
        for i in range(1, len(nums)):
            if target - nums[i] in curr: return [curr[target - nums[i]], i]
            curr[nums[i]] = i