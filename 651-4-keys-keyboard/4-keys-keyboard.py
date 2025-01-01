class Solution:
    def maxA(self, n: int) -> int:
        #some sort of bottom up dp
        @lru_cache(None)
        def bt(curr, cb, cnt):
            if curr >= n - 3:
                return cnt + (n - curr) * cb
            return max(bt(curr + 3, cnt, cnt*2), bt(curr + 1, cb, cnt + cb))
        
        return bt(0, 1, 0)