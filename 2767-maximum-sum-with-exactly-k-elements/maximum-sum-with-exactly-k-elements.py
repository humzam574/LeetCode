class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        num = max(nums)
        total = 0

        for i in range(k):
            total += num + i

        return total