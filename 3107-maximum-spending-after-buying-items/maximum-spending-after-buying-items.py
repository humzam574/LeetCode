class Solution:
    def maxSpending(self, v): return sum(starmap(mul, zip(sorted(chain(*v)), count(1))))