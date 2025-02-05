class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = [0] * len(s)
        for i in range(len(s)):
            arr[i] = abs(ord(s[i]) - ord(t[i]))
        ans = 0
        l = 0
        curr = 0
        for r in range(len(s)):
            curr += arr[r]
            while l <= r and curr > maxCost:
                curr -= arr[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans