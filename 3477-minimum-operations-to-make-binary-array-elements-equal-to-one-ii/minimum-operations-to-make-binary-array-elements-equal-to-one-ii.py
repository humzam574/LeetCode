class Solution:
    def minOperations(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            if (num + curr) % 2 == 0: curr += 1
        return curr