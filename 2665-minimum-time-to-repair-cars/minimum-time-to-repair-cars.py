class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, min(ranks) * cars * cars
        while l < r:
            m = (l + r) // 2
            if sum(int(math.sqrt(m/v)) for v in ranks) < cars: l = m + 1
            else: r = m
        return l