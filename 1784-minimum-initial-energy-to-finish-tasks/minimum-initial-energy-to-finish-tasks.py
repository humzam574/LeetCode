class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x : x[0] - x[1])
        curr = 0
        tot = 0
        for a, b in tasks:
            if b > curr:
                tot += (b - curr)
                curr = b
            curr -= a
        return tot