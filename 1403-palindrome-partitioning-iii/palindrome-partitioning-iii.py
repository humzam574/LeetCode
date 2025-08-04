class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        #2ddp
        #x is the idx of s
        #y is how many cuts you can make
        
        n = len(s)

        dp = [[0] *n for _ in range(k)]
        memo = {}
        for l in range(n):
            arr = [s[l]]
            memo[(l,l)] = 0
            for r in range(l+1, n):
                arr.append(s[r])
                diff = 0
                ls, rs = l, r
                while ls < rs:
                    if s[ls] != s[rs]:
                        diff+=1
                    ls+=1
                    rs-=1
                memo[(l, r)] = diff
        for i in range(n):
            dp[0][i] = memo[(0, i)]
        for j in range(1, k):
            for i in range(j+1, n):
                mx = dp[j-1][i-1] + 1
                for l in range(j-1, i):
                    mx = min(mx, dp[j-1][l] + memo[(l+1,i)])
                dp[j][i] = mx

        return dp[-1][-1]