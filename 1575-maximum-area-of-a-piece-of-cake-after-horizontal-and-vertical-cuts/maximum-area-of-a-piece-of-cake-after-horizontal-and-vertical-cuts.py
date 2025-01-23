class Solution:
    def maxArea(self, h: int, w: int, hor: List[int], ver: List[int]) -> int:
        hor.sort(); ver.sort(); hor.append(h); ver.append(w); hor.append(0); ver.append(0); d1, d2, n = 0, 0, 1000000007
        for i in range(len(hor)): d1 = max(d1, hor[i] - hor[i - 1])
        for i in range(len(ver)): d2 = max(d2, ver[i] - ver[i - 1])
        return (d1%n) * (d2%n) % n