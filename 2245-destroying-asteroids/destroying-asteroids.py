class Solution:
    def asteroidsDestroyed(self, m, s): return all(m:=m+a if m>=a else False for a in sorted(s))