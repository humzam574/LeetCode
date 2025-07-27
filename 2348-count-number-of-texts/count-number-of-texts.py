class Solution:
    def countTexts(self, s: str) -> int:
        #7 and 9 are 4's
        l = 0
        n = len(s)
        mod = 1000000007
        ans = 1
        self.memo = [{1: 1, 2: 2, 3: 4}, {1: 1, 2: 2, 3: 4, 4: 8}]
        def dp(i, curr):
            if curr <= 0:
                return 0
            if curr in self.memo[i]:
                return self.memo[i][curr]
            val = dp(i, curr-1) + dp(i, curr-2) + dp(i, curr-3)
            if i:
                val+=dp(i, curr-4)
            val%=1000000007
            self.memo[i][curr] = val
            return val

        for r in range(n):
            if s[r] != s[l]:
                if s[l] == '7' or s[l] == '9':
                    ans = ans * dp(1, r-l)
                else:
                    ans = ans * dp(0, r-l)
                l = r
                ans%=mod
                # print(ans)
        #do it for the last one
        # print("l: " + str(l))
        # print("r: " + str(r))
        if l < r:
            if s[l] == '7' or s[l] == '9':
                ans = ans * dp(1, r-l + 1)
            else:
                ans = ans * dp(0, r-l + 1)
        return ans%mod