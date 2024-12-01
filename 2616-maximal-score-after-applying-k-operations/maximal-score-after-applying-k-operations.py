class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap, ans = [-n for n in nums], 0
        heapify(heap)
        for i in range(k):
            temp = heappop(heap)
            ans -= temp
            heappush(heap, temp//3)
        return ans