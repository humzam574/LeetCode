class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        heap = []
        for r in [reward1[i] - reward2[i] for i in range(len(reward1))]:
            heapq.heappush(heap, r)
            if len(heap) > k: heapq.heappop(heap)
        return sum(reward2) + sum(heap)