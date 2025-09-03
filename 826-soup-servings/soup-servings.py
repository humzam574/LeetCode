class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1
        
        n = (n+24) // 25
        dp = [[0] * n for _ in range(n)]
        #1, 1 = 0.25 + 0.25/2 + 0.25/2 + 0.25/2
        #2, 1 = 0.25 + 0.25/2 + 0.25 + 0
        #3, 1 = 0.25 + 0.25/2 + 0 + 0
        #4, 1 = 0.25
        #1, 2 = 0.25 + 0.25/2 + 0.25/2
        #1,3 = 0.25 + 0.25 


        #2,2 = 0.25 + 0.25 + (0.25/2)

        memo = {}
        # @cache
        @lru_cache(maxsize=None)
        def dp(a, b):
            # print(str(a) + ", " + str(b))
            if a <= 0 and b <= 0:
                # print("0.5")
                # print()
                return 0.5
            elif a <= 0:
                # print("1")
                # print()
                return 1
            elif b <= 0:
                # print("0")
                # print()
                return 0
            
            return 0.25*dp(a-4,b) + 0.25*dp(a-3,b-1) + 0.25*dp(a-2,b-2) + 0.25*dp(a-1,b-3)
        return dp(n,n)