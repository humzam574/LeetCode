class Solution:
    def waysToSplitArray(self, n):l,r,ans=0,(sum(n)+1)//2,0;return sum((l:=l+n[i])>=r for i in range(len(n)-1))