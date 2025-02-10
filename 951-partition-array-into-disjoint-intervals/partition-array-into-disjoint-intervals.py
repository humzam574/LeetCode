class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        #a prefix and a suffix
        #prefix tracks the highest value at or before i
        #suffix tracks the lowest number after i
        #1000001
        prefix = [-1] * len(nums)
        prefix[0] = nums[0]
        suffix = [1000001] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = max(prefix[i - 1], nums[i])
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i + 1])
        #print(prefix)
        #print(suffix)
        for i in range(len(nums)):
            if prefix[i] <= suffix[i]:
                return min(len(nums) - 1, i + 1)
        return -1