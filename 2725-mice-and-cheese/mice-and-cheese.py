class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        heap = []
        #for i in range(len(reward1)):
        rw = [reward1[i] - reward2[i] for i in range(len(reward1))]
        #print(rw)
        for r in rw:
            heapq.heappush(heap, r)  # Push negative value
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the smallest (most negative)
        print(heap)
        return sum(reward2) + sum(heap)