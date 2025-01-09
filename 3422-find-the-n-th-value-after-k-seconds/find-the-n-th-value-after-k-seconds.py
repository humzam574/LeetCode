class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return comb(k+n-1,n-1) % 1000000007