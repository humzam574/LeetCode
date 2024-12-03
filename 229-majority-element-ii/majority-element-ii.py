class Solution:
    def majorityElement(self, s): return [n for n, c in Counter(s).items() if c > len(s) // 3]
