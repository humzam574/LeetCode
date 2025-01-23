class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = pow(10,9) + 7
        def max_interval(length:int, cuts: List[int]) -> int:
            max_interval = 0
            cuts.sort()
            prev = 0
            for cut in cuts:
                if cut - prev > max_interval:
                    max_interval = max(cut - prev, max_interval)
                prev = cut
            max_interval = max(length - prev, max_interval)
            return max_interval
        horizontal_max_interval = max_interval(h, horizontalCuts) % mod
        vertical_max_interval = max_interval(w, verticalCuts) % mod
        return (horizontal_max_interval * vertical_max_interval) % mod
