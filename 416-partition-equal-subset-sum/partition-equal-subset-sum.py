class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, dp = sum(nums), 1 << 0
        if total % 2: return False
        for num in nums: dp |= dp << num
        return (dp & (1 << total // 2)) != 0