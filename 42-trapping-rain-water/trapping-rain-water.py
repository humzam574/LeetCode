class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l = 0
        def compute(l, r):
            m = min(height[l], height[r])
            val = 0
            for i in range(l + 1, r):
                val += (m - height[i])
                height[i] = m
            # print("l: " + str(l))
            # print("r: " + str(r))
            # print("v: " + str(val))
            # print()
            return val
        for r in range(len(height)):
            if height[r] >= height[l]:
                ans+=compute(l, r)
                l = r
        r = len(height) - 1
        for l in range(len(height) - 1, -1, -1):
            if height[l] >= height[r]:
                ans += compute(l, r)
                r = l
        return ans