class Solution:
    def maximumCoins(self, A: List[List[int]], k: int) -> int:
        def slide(A):
            A.sort()
            res = cur = j = 0
            for i in range(len(A)):
                cur += (A[i][1] - A[i][0] + 1) * A[i][2]
                while A[j][1] < A[i][1] - k + 1:
                    cur -= (A[j][1] - A[j][0] + 1) * A[j][2]
                    j += 1
                part = max(0, A[i][1] - k - A[j][0] + 1) * A[j][2]
                res = max(res, cur - part)
            return res
        return max(slide(A), slide([[-r,-l,w] for l,r,w in A]))