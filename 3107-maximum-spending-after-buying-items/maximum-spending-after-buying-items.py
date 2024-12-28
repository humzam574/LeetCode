class Solution:
    def maxSpending(self, values):
        n = len(values[0])
        heap = [(row[-1], i, n - 1) for i, row in enumerate(values)]
        heapify(heap)
        ans = d = 0
        while heap:
            d += 1
            v, i, j = heappop(heap)
            ans += v * d
            if j:
                heappush(heap, (values[i][j - 1], i, j - 1))
        return ans