class Solution:
    def prefixCount(self,w,p):return sum(w[i].startswith(p)for i in range(len(w)))