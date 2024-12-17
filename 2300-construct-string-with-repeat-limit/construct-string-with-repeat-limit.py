class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap, ans = [(-ord(k), v) for k, v in Counter(s).items()], ""
        heapify(heap)
        while heap:
            k, v = heappop(heap)
            if v <= repeatLimit:
                ans+=(chr(-k) * v)
            else:
                ans+=(chr(-k) * repeatLimit)
                if not heap: break
                ok, ov = heappop(heap)
                ans+=chr(-ok)
                if ov > 1:
                    heappush(heap, (ok, ov - 1))
                heappush(heap, (k, v - repeatLimit))
        return ans