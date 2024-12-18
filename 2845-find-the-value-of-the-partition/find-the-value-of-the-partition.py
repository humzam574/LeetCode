class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        return min(b - a for a, b in zip(sorted(nums), sorted(nums)[1:]))