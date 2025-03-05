class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = sum(data) #represents window size
        if k <= 1: return 0
        current = sum(data[:k])
        swaps = k - current

        for r in range(k, len(data)):
            left, right = data[r - k], data[r]
            current -= left - right
            if k - current < swaps:
                swaps = k - current
        return swaps