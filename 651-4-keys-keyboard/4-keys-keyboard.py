class Solution:
    def maxA(self, n: int) -> int:
        c= (n//5) + 1
        if n < 15:
            if n==5: return 5
            if n==10: return 20
            r=(n + 1)%c
            q=((n + 1)//c) - 1
            return q**(c - r)*(q + 1)**r
        else:
            r = n % 5
            return 3**(4 - r)*4**(c - 4 + r)