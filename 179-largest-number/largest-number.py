class Solution:
    def largestNumber(self,s):return str(int(''.join([str(n)for n in sorted(s,key=lambda x:x/(10**len(str(x))-1),reverse=True)])))