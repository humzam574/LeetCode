class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-v for v in gifts]
        heapify(heap)
        for i in range(k): heapq.heappush(heap, -math.floor((-heapq.heappop(heap)) ** 0.5))
        return -sum(heap)