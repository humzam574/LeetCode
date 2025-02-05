class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr, ans, l, curr = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))], 0, 0, 0
        for r in range(len(s)):
            curr += arr[r]
            while l <= r and curr > maxCost: curr, l = curr - arr[l], l + 1
            ans = max(ans, r - l + 1)
        return ans