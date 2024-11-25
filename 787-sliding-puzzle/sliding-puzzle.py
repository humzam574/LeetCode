class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        fin = [[1,2,3],[4,5,0]]
        self.low = int(1e9)
        vis = defaultdict(int)
        def search(x,y,dep):
            if dep <= self.low:
                #print("dep = " + str(dep))
                #print(board)
                if board == fin:
                    return dep
                sig =(''.join(str(n) for n in board[0])) + (''.join(str(n) for n in board[1]))
                #print(sig)
                if sig in vis and vis[sig] < dep:
                    return -1
                vis[sig] = dep
                found = False
                direct = [(0,1),(1,0),(-1,0),(0,-1)]
                for (dx,dy) in direct:
                    if 0 <= x+dx < 2 and 0 <= y+dy < 3:
                        board[x+dx][y+dy], board[x][y] = board[x][y], board[x+dx][y+dy]
                        #if vis[(''.join(str(n) for n in board[0])) + (''.join(str(n) for n in board[1]))] >= dep:
                        answer = search(x+dx, y+dy, dep+1)
                        if answer != -1:
                            #print(self.low)
                            self.low = min(self.low, answer)
                            found = True
                        board[x+dx][y+dy], board[x][y] = board[x][y], board[x+dx][y+dy]
                if not found:
                    return -1
                return self.low
            return -1
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return search(i,j,0)
            