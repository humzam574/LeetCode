class Solution:
    def halveArray(self, heap: List[int]) -> int:
        target, curr, heap, ans = sum(heap) / 2, 0, [-n for n in heap], 0
        heapify(heap)
        while curr < target:
            v = -1 * heappop(heap) / 2
            curr, ans = curr + v, ans + 1
            heappush(heap, -v)
        return ans