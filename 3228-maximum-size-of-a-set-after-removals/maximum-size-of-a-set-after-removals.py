class Solution:
    def maximumSetSize(self, nums1, nums2):
        s1, s2, n = set(nums1), set(nums2), len(nums1)
        x = len(s1)
        ans = min(n // 2, x)
        rem, c, t = x - ans, ans, n // 2 + ans
        for i in s2:
            if i not in s1: c += 1
            elif rem > 0: c, rem = c + 1, rem - 1
            if c >= t: break
        return c