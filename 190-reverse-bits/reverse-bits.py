class Solution:
    def reverseBits(self,n):
        n=bin(n)[2:].zfill(32)
        #,print(n)
        n=n[::-1]
        return int(n,2)