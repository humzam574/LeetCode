class Solution:
    def rotate(self, n, k): k %= len(n); n.reverse(); n[k:], n[:k] = reversed(n[k:]), reversed(n[:k])