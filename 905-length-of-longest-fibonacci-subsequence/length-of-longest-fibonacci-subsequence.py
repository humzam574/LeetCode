class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        search = set(arr)
        n = len(arr)
        memo = defaultdict(int)#{}  # Explicit memoization dictionary
        def fib(x, y):
            if (x, y) in memo:  # Check if already computed
                return memo[(x, y)]
            
            if (x + y) in search:
                memo[(x, y)] = 1 + fib(max(x, y), x + y)
                return memo[(x, y)]
            
            #memo[(x, y)] = 0
            return 0

        # Iterate through all x, y pairs, decrementing j
        for i in range(n):
            for j in range(n - 1, i, -1):  # j now decrements instead of incrementing
                ans = max(ans, 2 + fib(arr[i], arr[j]))

        return ans if ans > 2 else 0
