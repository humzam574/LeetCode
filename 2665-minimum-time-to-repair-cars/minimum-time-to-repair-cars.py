class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        left = 0
        right = 100 * ceil(cars / n)**2
        ranks = Counter(ranks)

        def f(x):
            result = 0
            for rank, v in ranks.items():
                result += v * isqrt(x // rank)
            return result

        while right - left != 1:
            mid = (2 * left + right) // 3
            mid += left == mid
            if f(mid) >= cars:
                right = mid
            else:
                left = mid
        return right