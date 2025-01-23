class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        curr = -nums[-1]
        suffix = [0] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        for i in range(n):
            curr += nums[i - 1]
            suffix[i] += (1 + 2*i - n)*nums[i] - curr
        return suffix