class Solution:
    def clumsy(self,n):return n if(n<3)else 6 if(n==3)else 7 if(n==4)else n+2-(n%4==0)if(n%4<3)else n-1