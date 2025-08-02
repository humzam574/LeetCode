class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        prefix = [0] * n
        for i in range(n):
            hours[i] = 1 if hours[i] > 8 else -1
            prefix[i] = prefix[i-1] + hours[i]
        print(hours)
        print(prefix)
        #keep track first point that has a given value
        points = {0: -1}
        for i, v in enumerate(prefix):
            if v not in points:
                if v-1 in points:
                    points[v] = min(i, points[v-1])
                else:
                    points[v] = i
        ans = 0
        for i, v in enumerate(prefix):
            if v - 1 in points:
                print(str(i) + ", " + str(i - points[v-1] + 1))
                ans = max(ans, i - points[v-1])
        return ans