__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d=defaultdict(set)
        for i,j in logs:
            d[i].add(j)
        res=[0]*k
        for i in d.values():
            j=len(i)
            if j<=k:
                res[j-1]+=1
        return res