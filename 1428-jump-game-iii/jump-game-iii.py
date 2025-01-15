def reach(ps, i, n):
    if i < 0 or i >= n: return False
    if ps[i] == 0:      return True
    if ps[i] == -1:     return False
    s = ps[i]; ps[i] = -1
    return reach(ps, i + s, n) or reach(ps, i - s, n)

class Solution:
    def canReach(self, ps: List[int], s: int) -> bool:
        return reach(ps, s, len(ps))