class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap, dq, t= [-val for val in Counter(tasks).values()], deque(), 0
        heapify(heap)
        while heap or dq:
            t += 1
            if heap:
                temp = 1 + heappop(heap)
                if temp: dq.append([temp, t+n])
            else: t = dq[0][1]
            if dq and dq[0][1] == t: heappush(heap, dq.popleft()[0])
        return t