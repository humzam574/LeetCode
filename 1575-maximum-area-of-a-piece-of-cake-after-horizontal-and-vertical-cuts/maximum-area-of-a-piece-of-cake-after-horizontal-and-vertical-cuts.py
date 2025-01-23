class Solution:
    def maxArea(self, h: int, w: int, hor: List[int], ver: List[int]) -> int:
        hor.sort()
        ver.sort()
        hor.append(h)
        hor.append(0)
        ver.append(w)
        ver.append(0)
        #find the largest delta of the two and multiply
        d1 = 0
        d2 = 0
        for i in range(0, len(hor)):
            d1 = max(d1, hor[i] - hor[i - 1])
        for i in range(0, len(ver)):
            d2 = max(d2, ver[i] - ver[i - 1])
        return d1 * d2 % (1000000007)