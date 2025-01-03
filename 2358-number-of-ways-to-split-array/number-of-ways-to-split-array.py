class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)): prefix[i] = prefix[i - 1] + nums[i]

        # 10, 4, -8, 7
        # 10, 14, 6, 13

        suffix = [0] * len(nums)
        # suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1): suffix[i] = suffix[i + 1] + nums[i + 1]

        # 10, 4, -8, 7
        # 3, -1, 7, 0
        print(prefix)
        print(suffix)

        return sum([prefix[i] >= suffix[i] for i in range(len(nums)-1)])