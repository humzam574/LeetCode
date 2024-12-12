class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-n for n in nums]
        target, curr = -sum(heap) / 2, 0
        heapify(heap)
        ans = 0
        while curr < target:
            v = heappop(heap)
            v = -1*v/2
            curr += v
            heappush(heap, -v)
            ans+=1
        return ans