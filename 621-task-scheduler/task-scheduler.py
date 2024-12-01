class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #maintain a list of recent tasks and whats pending
        dict = Counter(tasks)
        heap = [-val for val in dict.values()]
        heapify(heap)
        dq = deque()
        t = 0
        while heap or dq:
            t += 1
            if heap:
                temp = 1 + heappop(heap)
                if temp:
                    dq.append([temp, t+n])
            else:
                t = dq[0][1]
            if dq and dq[0][1] == t:
                heappush(heap, dq.popleft()[0])
        return t