class Solution:
    def maximumProduct(self, heap: List[int], k: int) -> int:
        heapify(heap); ans = 1
        for i in range(k): heappush(heap, heappop(heap)+1)
        for item in heap: ans = (ans * item) % (10**9 + 7)
        return ans# % (10**9 + 7)