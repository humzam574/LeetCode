class Solution:
    def minFlips(self, G: List[List[int]]) -> int:
        M, N = len(G), len(G[0])
        P = [(i,j) for i,j in itertools.product(range(M),range(N))]
        for n in range(M*N+1):
            for p in itertools.permutations(P,n):
                H = list(map(list,G))
                for (x,y) in p:
                    for (i,j) in (x,y-1),(x,y),(x,y+1),(x-1,y),(x+1,y):
                        if 0 <= i < M and 0 <= j < N: H[i][j] = 1 - H[i][j]
                if max(max(H)) == 0: return n
        return -1