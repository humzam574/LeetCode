class Solution:
    def minCost(self, colors: str, need: List[int]) -> int:
        ans = 0
        high = -1
        tot = 0
        group = False
        for i in range(len(colors) - 1):
            if colors[i] == colors[i+1]:
                if not group:
                    tot+=need[i]
                tot+=need[i+1]
                high = max(high, need[i], need[i+1])
                group = True
            else:
                if group:
                    ans+=(tot-high)
                group = False
                high = -1
                tot = 0
        # print(tot)
        # print(high)
        if group:
            ans+=(tot-high)
        # print(ans)
        # print(curr)
        return ans