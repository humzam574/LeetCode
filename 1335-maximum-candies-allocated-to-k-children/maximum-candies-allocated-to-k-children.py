class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        #you can divide each pile candies[i] into any number of sub piles
        #allocate piles of candies into k children so each child gets equal candies
        #each child can be allocated from only one pile

        #binary search
        #candies.sort(reverse = True)
        if k > sum(candies):
            return 0
        def check(x):
            # n = len(candies)
            # i = 0
            # while x > 0 and i < n:
            #     x -= candies[i]//k
            #     i += 1
            # return x
            return sum(c // x for c in candies)
        l, r = 1, max(candies)
        ans = 0
        while l <= r:
            m = (l + r) // 2
            v = check(m)
            if v >= k:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
