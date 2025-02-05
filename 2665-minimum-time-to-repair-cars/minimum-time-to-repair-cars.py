class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks) * cars * cars
        while l < r:
            m = (l + r) // 2
            if sum(math.floor((m/v)**(0.5)) for v in ranks) < cars: l = m + 1
            else: r = m
        return l