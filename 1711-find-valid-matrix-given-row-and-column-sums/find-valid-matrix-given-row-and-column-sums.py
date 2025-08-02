class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        #[5,7,10]
        #[8,6,8]

        #[5, 0, 0]
        #[3, 4, 0]
        #[0, 2, 8]

        #[3, 8]
        #[4, 7]
        
        #[3, 0]
        #[1, 7]

        #cant i just do a greedy approach

        ans = [[0] * len(colSum) for _ in range(len(rowSum))]
        m = len(colSum)
        n = len(rowSum)
        for i in range(n):
            curr = ans[i]
            rem = rowSum[i]
            rowSum[i] = 0
            for j in range(m):
                curr[j] += min(rem, colSum[j])
                rem -= curr[j]
                colSum[j] -= curr[j]
            ans[i] = curr
        # for row in ans:
        #     print(row)
        return ans