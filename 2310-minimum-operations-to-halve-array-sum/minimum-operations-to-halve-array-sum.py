class Solution:
    def halveArray(self, heap: List[int]) -> int:
        target, curr, heap, ans = sum(heap) / 2, 0, [-n for n in heap], 0; heapify(heap)
        while True:
            v = heappop(heap) / 2; curr, ans = curr - v, ans + 1; heappush(heap, v)
            if curr >= target: return ans