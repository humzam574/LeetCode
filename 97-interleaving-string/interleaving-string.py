class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #memoized dp
        self.x, self.y, self.z = len(s1), len(s2), len(s3)
        if self.x + self.y != self.z:
            return False
        @cache
        def dp(i, j, k):
            if k == self.z:
                return (i == self.x and j == self.y)
            if i == self.x:
                #return self.y - j == self.z - k and s2[j:] == s3[k:]
                return s2[j:] == s3[k:]
            if j == self.y:
                #return self.x - i == self.z - k and s1[i:] == s3[k:]
                return s1[i:] == s3[k:]
            if s1[i] == s3[k] and s2[j] == s3[k]:
                return dp(i + 1, j, k + 1) or dp(i, j + 1, k + 1)
            elif s1[i] == s3[k]:
                return dp(i + 1, j, k + 1)
            elif s2[j] == s3[k]:
                return dp(i, j + 1, k + 1)
            return False
        return dp(0, 0, 0)
