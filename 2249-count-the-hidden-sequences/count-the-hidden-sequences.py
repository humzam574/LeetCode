class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low = 0
        high = 0
        curr = 0
        for d in differences:
            curr+=d
            if curr > high:
                high = curr
            if curr < low:
                low = curr
        delta = upper - lower - 1
        hl = high - low - 1
        return max(0, upper - high - lower + low + 1)