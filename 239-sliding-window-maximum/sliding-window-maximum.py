class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        heap = [(-val, i) for i, val in enumerate(nums[:k])]
        heapq.heapify(heap)
        ans = [-heap[0][0]]
        for i in range(k, len(nums)):
            while heap[0][1] <= i - k: heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i], i))
            ans.append(-heap[0][0])
        return ans
