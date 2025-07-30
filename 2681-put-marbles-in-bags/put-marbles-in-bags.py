class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        #split weights up into k subarrays
        #first maximize the l and r of the subarrays
        #then minimize the l and r
        #alternatively, you need the 0th and n-1th element as part of your weights
        #and you're picking groups of two numbers in weights which you need to maximize
        #so you need to pick k-1 pairs inside weights
        n = len(weights)
        maxheap = []
        minheap = []
        heapify(maxheap)
        heapify(minheap)
        # k -= 1
        length = 0
        for i in range(1, n):
            #first maximize
            heappush(maxheap, -weights[i]-weights[i-1])
            heappush(minheap, weights[i] + weights[i-1])
            if i >= k:
                heappop(maxheap)
                heappop(minheap)
        # high = sum(heap)
        # print(maxheap)
        # print(minheap)
        return sum(minheap) + sum(maxheap)