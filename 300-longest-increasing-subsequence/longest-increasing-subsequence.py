class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dep = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dep[i] = max(dep[i], 1 + dep[j])
        return max(dep)