class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:k-1]
        #print(colors)
        prev = 0
        ans = 0
        for i in range(1, len(colors)):
            #print("i: " + str(i) + ", prev: " + str(prev) + ", ans = " + str(ans))
            if colors[i] == colors[i - 1]:
                if i - prev + 1 > k:
                    ans += (i - prev + 1 - k)
                # elif i - prev + 1 == k:
                #     ans += 1
                prev = i
        return ans + max((i - prev + 2 - k), 0)