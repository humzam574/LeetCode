class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while nums[0] < k:
            count += 1
            one = heappop(nums)
            two = heappop(nums)
            heappush(nums, one*2 + two)
        return count