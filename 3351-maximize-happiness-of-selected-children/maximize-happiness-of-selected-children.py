class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for h in happiness:
            heappush(heap, -h)
        ans = 0
        for i in range(k):
            a = -heappop(heap)
            if a <= i:
                return ans
            ans+=a-i
        return ans