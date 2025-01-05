class Solution:
    def stringShift(self,s,h):return(lambda i:s[i:]+s[:i])(sum(x*(1-2*d)for d,x in h)%len(s))