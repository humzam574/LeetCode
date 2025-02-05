class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first, last, prev, high = 20000, -1, -1, -1
        for i in range(len(seats)):
            if seats[i]: last, first, high, prev = i, min(first, i), max(high, i - prev), i
        return max(high // 2, i - last, first)
