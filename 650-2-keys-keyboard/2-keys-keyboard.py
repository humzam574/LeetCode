class Solution:
    def minSteps(self,n):return next((self.minSteps(n//i)+i for i in range(2,isqrt(n)+1)if n%i<1),(0,n)[n>1])
