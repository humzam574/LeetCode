class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)

        while l < r:
            # print(str(l) + ", " + str(r))
            m = (l + r) // 2
            if m == 0:
                return 1
            curr = 0
            for pi in piles:
                curr += (pi + m - 1) // m
            if curr <= h:
                r = m
            else:
                l = m + 1
            
        return r