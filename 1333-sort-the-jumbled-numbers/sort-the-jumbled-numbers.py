class Solution:
    def sortJumbled(self,m,n):
        m={str(i):str(j) for i,j in enumerate(m)}
        return sorted(n,key=lambda a:int("".join(map(m.get,str(a)))))