class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        prefix = [[0] * n for _ in range(m)]

        # for row in mat:
        #     print(row)
        # print()
        # print()

        for i in range(m):
            prefix[i][0] = mat[i][0]
            for j in range(1, n):
                prefix[i][j] = 0 if not mat[i][j] else prefix[i][j-1] + 1
        
        # for row in prefix:
        #     print(row)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if prefix[i][j] == 0:
                    continue
                # print(str(i) + ", " + str(j))
                ans+=prefix[i][j]
                k = i - 1
                low = inf
                while k >= 0 and prefix[k][j] > 0:
                    # print(str(k) + ", " + str(j))
                    low = min(low, prefix[k][j], prefix[i][j])
                    ans+=low#min(prefix[k][j], prefix[i][j])
                    k -= 1
        
        return ans
                