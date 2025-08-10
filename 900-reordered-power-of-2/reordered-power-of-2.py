class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_sorted = set(''.join(sorted(str(1 << i))) for i in range(31))
        n_sorted = ''.join(sorted(str(n)))
        return n_sorted in power_sorted

        