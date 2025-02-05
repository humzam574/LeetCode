class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        min_cost = [0, 0, 0]
        for index, num in enumerate(nums):
            min_cost[index % 3] = min(min_cost) + (0 if num >= k else (k - num))
        return min(min_cost)