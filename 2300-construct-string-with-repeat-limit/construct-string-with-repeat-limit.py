class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap, ans = [[-ord(k), v] for k, v in Counter(s).items()], ""
        heapify(heap)
        while heap:
            k, v = heappop(heap)
            if v <= repeatLimit: ans+=(chr(-k) * v)
            else:
                ans+=(chr(-k) * repeatLimit)
                if not heap: break
                ans+=chr(-heap[0][0])
                if heap[0][1] == 1: heappop(heap)
                else: heap[0][1] -= 1
                heappush(heap, [k, v - repeatLimit])
        return ans