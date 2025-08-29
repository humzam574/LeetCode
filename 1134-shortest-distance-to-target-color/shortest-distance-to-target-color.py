class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        self.arrs = [[], [], [], []]
        for i, c in enumerate(colors):
            self.arrs[c].append(i)
        for row in self.arrs[1:]:
            print(row)
        
        def bsearch(target, n):
            if not self.arrs[n]:
                return -1
            l = bisect.bisect_left(self.arrs[n], target)
            r = bisect.bisect_right(self.arrs[n], target)
            # print(target)
            # print(self.arrs[n])
            # print(l)
            # print(r)
            # print()
            if r >= len(self.arrs[n]):
                r-=1
            if l >= len(self.arrs[n]):
                l-=1
            return min(abs(target - self.arrs[n][l]), abs(target - self.arrs[n][r]), abs(target - self.arrs[n][l-1]))
        
        ans = []
        for a, b in queries:
            ans.append(bsearch(a,b))
        return ans