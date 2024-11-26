class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = set()
        tot = set([i for i in range(n)])
        for edge in edges:
            # if edge[0] in losers:
            #     tot.remove(edge[1])
            # if edge[0] not in losers:
            #     losers.add(edge[1])
            #if edge[1] in tot:
            tot.discard(edge[1])
        # print(losers)
        # print(tot)
        # for l in losers:
        #     tot.remove(l)
        if len(tot) > 1 or len(tot) == 0:
            return -1
        return tot.pop()
            
                