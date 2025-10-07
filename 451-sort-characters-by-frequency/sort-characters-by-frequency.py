from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        min_heap = []
        res = ""
        for char, freq in counter.items():
            heapq.heappush(min_heap,[-freq,char])
        while min_heap:
            v, c = heapq.heappop(min_heap)
            res = res + c * (-v)

        return res 
        
        