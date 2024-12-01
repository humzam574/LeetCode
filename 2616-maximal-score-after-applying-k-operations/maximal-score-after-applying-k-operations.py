class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # def ceil(n):
        #     if n % 3 == 0:
        #         return n//3
        #     else:
        #         return n//3
        heap = [-n for n in nums]
        heapify(heap)
        ans = 0
        for i in range(k):
            temp = heappop(heap)
            ans-=temp
            heappush(heap, temp//3)
        return ans