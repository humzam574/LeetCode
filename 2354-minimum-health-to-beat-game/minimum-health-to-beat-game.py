class Solution:
    def minimumHealth(self,d,a):return 1+sum(d)-min(a,max(d))