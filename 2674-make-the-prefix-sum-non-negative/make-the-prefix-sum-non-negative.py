class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        heap = []
        heapify(heap)
        for n in nums:
            curr += n
            if n < 0:
                heappush(heap, n)
            if curr < 0:
                curr -= heappop(heap)
                ans += 1
        return ans