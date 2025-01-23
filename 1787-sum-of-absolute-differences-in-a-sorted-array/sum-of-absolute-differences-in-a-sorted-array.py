class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        s = sum(nums)
        for i in range(length):
            result.append(s + nums[i] *(2 * i - length))
            s = s - 2*nums[i]
        return result