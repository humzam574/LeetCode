class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)
        for n in range(k):
            n, i = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))
        return nums