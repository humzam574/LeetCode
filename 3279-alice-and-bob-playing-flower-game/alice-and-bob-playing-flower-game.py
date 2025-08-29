class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        #n is odd m is even
        #n is even m is odd
        
        nodd = (n+1) // 2
        
        neven = (n)//2
        modd = (m+1) // 2
        meven = (m)//2

        # print(nodd)
        # print(neven)
        # print(modd)
        # print(meven)

        return nodd*meven + neven*modd