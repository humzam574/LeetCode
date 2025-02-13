class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while nums[0] < k:
            count += 1
            heappush(nums, heappop(nums)*2 + heappop(nums))
        return count