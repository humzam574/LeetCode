class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        def possible(xl, xh, yl, yh):
            d = -4
            for pt in points:
                if xl <= pt[0] <= xh and yl <= pt[1] <= yh:
                    d+=1
            return not bool(d)
        ans = -1
        memo = {}
        ln = len(points)
        for i in range(ln):
            for j in range(i + 1, ln):
                for k in range(j + 1, ln):
                    for l in range(k + 1, ln):
                        if (i, j, k, l) not in memo:
                            xl = min(points[i][0], points[j][0], points[k][0], points[l][0])
                            xh = max(points[i][0], points[j][0], points[k][0], points[l][0])
                            xst = set([points[i][0], points[j][0], points[k][0], points[l][0]])
                            yst = set([points[i][1], points[j][1], points[k][1], points[l][1]])
                            yl = min(points[i][1], points[j][1], points[k][1], points[l][1])
                            yh = max(points[i][1], points[j][1], points[k][1], points[l][1])
                            ps = possible(xl, xh, yl, yh)
                            if len(xst) == 2 and len(yst) == 2 and possible(xl, xh, yl, yh):
                                ans = max(ans, (xh - xl)*(yh - yl))
                            memo[(i,j,k,l)] = True
        if ans == 0:
            return -1
        return ans