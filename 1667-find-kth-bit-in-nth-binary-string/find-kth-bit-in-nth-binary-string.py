class Solution:
    def findKthBit(self, N: int, K: int, R = True) -> str:
        if K == 1: return '0' if R else '1'
        mid = (1 << (N - 1))
        if K == mid: return '1' if R else '0'
        if K < mid: return self.findKthBit(N - 1, K, R)
        return self.findKthBit(N - 1, 2 * mid - K, not R)