class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(k), v) for k, v in Counter(s).items()]
        heapify(heap)
        ans = []
        while heap:
            k, v = heappop(heap)
            if v <= repeatLimit:
                ans.append(chr(-k) * v)
            else:
                ans.append(chr(-k) * repeatLimit)
                if not heap:
                    break
                ok, ov = heappop(heap)
                ans.append(chr(-ok))
                if ov > 1:
                    heappush(heap, (ok, ov - 1))
                heappush(heap, (k, v - repeatLimit))
        return ''.join(ans)