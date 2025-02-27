class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        search = set(arr)
        n = len(arr)
        #iterate through all x,y combos
        #if x+y exists, do a search of y+(x+y) and so on

        def fib(x, y):
            #stuff
            if (x + y) in search:
                return 1 + fib(max(x, y), x + y)
            return 0
        
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, 2 + fib(arr[i], arr[j]))

        
        return ans if ans > 2 else 0