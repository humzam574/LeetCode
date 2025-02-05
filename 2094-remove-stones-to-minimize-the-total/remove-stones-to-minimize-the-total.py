class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]; heapify(heap)
        for i in range(k):
            t = -heappop(heap); t = t - t//2
            if t == 0: return 0
            heappush(heap, -t)
        return -sum(heap)