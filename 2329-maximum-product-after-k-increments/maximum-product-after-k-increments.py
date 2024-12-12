class Solution:
    def maximumProduct(self, heap: List[int], k: int) -> int:
        heapify(heap); ans = 1
        for i in range(k): heappush(heap, heappop(heap) + 1)
        return reduce(lambda ans, item: ans * item % (10**9 + 7), heap, ans)