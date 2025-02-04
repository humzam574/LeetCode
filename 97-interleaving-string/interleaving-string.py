class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.x, self.y, self.z = len(s1), len(s2), len(s3)
        @cache
        def dp(i, j, k): return (i == self.x and j == self.y) if k == self.z else s2[j:] == s3[k:] if i == self.x else s1[i:] == s3[k:] if j == self.y else dp(i + 1, j, k + 1) or dp(i, j + 1, k + 1) if s1[i] == s3[k] and s2[j] == s3[k] else dp(i + 1, j, k + 1) if s1[i] == s3[k] else dp(i, j + 1, k + 1) if s2[j] == s3[k] else False
        return dp(0, 0, 0)
