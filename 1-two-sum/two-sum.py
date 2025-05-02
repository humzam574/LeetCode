class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for key, value in enumerate(nums):
            if (target - value) in dict:
                ans = [dict[target - value], key]
                return ans
            elif value not in dict:
                dict[value] = key