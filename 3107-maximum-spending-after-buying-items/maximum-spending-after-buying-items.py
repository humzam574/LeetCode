class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        #heapify it
        heap = [shop[-1] for shop in values]
        dict = defaultdict(list)
        for i, shop in enumerate(values): dict[shop[-1]].append(i)
        heapify(heap)
        ans = 0
        for i in range(1, 1 + len(values) * len(values[0])):
            val = heappop(heap)
            ans += (i * val)
            idx = dict[val].pop()
            #print(idx)
            values[idx].pop()
            if values[idx]:
                dict[values[idx][-1]].append(idx)
                heappush(heap, values[idx][-1])
        return ans