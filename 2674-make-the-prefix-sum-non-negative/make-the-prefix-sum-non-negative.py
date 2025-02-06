class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        curr, ans, heap = 0, 0, []; heapify(heap)
        for n in nums:
            curr += n
            if n < 0: heappush(heap, n)
            if curr < 0: curr, ans = curr - heappop(heap), ans + 1
        return ans