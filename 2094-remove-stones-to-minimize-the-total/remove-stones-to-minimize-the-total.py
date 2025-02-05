class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)
        for i in range(k):
            t = -heappop(heap)
            
            if t == 0:
                break
            #ans = ans - t + t//2
            t = t - t // 2
            heappush(heap, -t)
        return -sum(heap)