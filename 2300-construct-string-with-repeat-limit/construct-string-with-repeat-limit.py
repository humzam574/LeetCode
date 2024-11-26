class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap, ans = [(-ord(ch), -c) for ch, c in Counter(s).items()], ''
        heapq.heapify(heap)
        while heap:
            mch, mc = heapq.heappop(heap)
            while heap and -mc > repeatLimit:
                tch, tc = heapq.heappop(heap)
                ans, mc = ans + chr(-mch) * repeatLimit + chr(-tch), mc + repeatLimit
                if tc < -1: heapq.heappush(heap, (tch, tc+1))
            ans += chr(-mch) * min(-mc, repeatLimit)
        return ans