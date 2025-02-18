class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)
        res=[i for i in range(1,n+2)]
        i=0
        while i<n:
            t=i
            while t< n and pattern[t]=="D":
                t+=1
            res[i:t+1] =reversed(res[i:t+1])
            if t!=i:
                i=t-1
            i+=1
        return "".join(map(str,res))