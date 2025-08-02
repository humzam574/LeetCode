alphabet = ascii_lowercase

class Solution:
    def minimizeStringValue(self, s: str)  -> str:

        ctr, dic = Counter(s), defaultdict(int)                 # <-- 1.
        qmarks = ctr['?']
        rep = lambda x, y: x.replace('?', y, dic[y] - ctr[y])

        heap = list(map(lambda x: (ctr[x],x), alphabet))        # <-- 2.
        heapify(heap)
        
        for _ in range(qmarks):                                 # <-- 3.
            cost, ch = heappop(heap)
            heappush(heap, (cost + 1, ch))

        for cost, ch in heap: dic[ch] = cost                    # <-- 4.

        return reduce(rep, alphabet, s)                         # <-- 5.