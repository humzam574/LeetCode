class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s) + 1):
            for j in range(i):
                temp = Counter(s[j:i])
                ans += max(temp.values()) - min(temp.values())
        return ans