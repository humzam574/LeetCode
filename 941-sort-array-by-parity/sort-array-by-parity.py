class Solution:
    def sortArrayByParity(self,n):return sorted(n,key=lambda x:x&1==1)