class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxReach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = 0 if i - r < 0 else i - r
            right = n if i + r > n else i + r
            maxReach[left] = right if right > maxReach[left] else maxReach[left]
        taps = curEnd = farthest = 0
        for i in range(n):
            farthest = maxReach[i] if maxReach[i] > farthest else farthest
            if i == curEnd:
                if farthest == curEnd:
                    return -1
                taps += 1
                curEnd = farthest
        return taps