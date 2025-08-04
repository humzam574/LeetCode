class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        #make a heap for the servers (weight, idx)
        #whenever you pop, set up a task in a second heap
        if len(servers) > 56:
            print(servers[36])
            print(servers[56])
        srv = [(w,i) for i,w in enumerate(servers)]
        heapify(srv)
        insert = []
        heapify(insert)
        ans = [0] * len(tasks)
        delta = 0
        for i,t in enumerate(tasks):
            if delta > 0:
                delta-=1
            while insert and insert[0][0] <= i+delta:
                tup = heappop(insert)
                heappush(srv, tup[1:])
            if not srv:
                delta = insert[0][0] - i
                while insert and insert[0][0] <= i+delta:
                    tup = heappop(insert)
                    heappush(srv, tup[1:])
            # if 145 < i < 149:
            #     print(str(i + delta))
            #     print(srv)
            #     print(insert)
            #     print()
            w, idx = heappop(srv)
            ans[i] = idx
            heappush(insert, (i+t+delta, w, idx))
        return ans