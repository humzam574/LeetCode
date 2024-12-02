class Solution:
    def maximumSetSize(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        n, x = len(nums1), len(s1)
        ans = min(n // 2, x)
        rem, c = x - ans, 0
        for i in s2:
            if i not in s1: c += 1
            elif rem > 0:
                c += 1
                rem -= 1
            if c >= n // 2: break
        return ans + c