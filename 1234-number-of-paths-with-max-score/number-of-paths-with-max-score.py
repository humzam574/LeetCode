class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        #2d dp for the first path to get the max score
        #another dp to find the number of ways... ?
        #brute force is 200!/(100!*100!) -> not possible
        n = len(board)

        dp = [[(0, 0)] * n for i in range(n)]
        dp[0][0] = (0, 1)
        # dp = [[0] * n for i in range(n)]
        board[0] = '0' + board[0][1:]
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if board[i][j] == 'X':
                    dp[i][j] = -999999
                    continue
                # pos = False
                #a, b = 0, defaultdict(int)
                a = 0
                b = 0
                if i != 0 and '0' <= board[i-1][j] <= '9':
                    # pos = True
                    # dp[i][j] = max(dp[i][j], dp[i - 1][j] + int(board[i-1][j]))
                    temp = dp[i-1][j][0] + ord(board[i-1][j]) - 48
                    # b[temp]+=dp[i-1][j][1]
                    # a = max(a, temp)
                    b = dp[i-1][j][1]
                    a = temp
                if j != 0 and '0' <= board[i][j-1] <= '9':
                    # pos = True
                    # dp[i][j] = max(dp[i][j], dp[i][j - 1] + int(board[i][j-1]))
                    temp = dp[i][j-1][0] + ord(board[i][j-1]) - 48
                    # b[temp]+=dp[i][j-1][1]
                    # a = max(a, temp)
                    if temp > a:
                        a = temp
                        b = dp[i][j-1][1]
                    elif temp == a:
                        b+=dp[i][j-1][1]
                if i != 0 and j != 0 and '0' <= board[i-1][j-1] <= '9':
                    # pos = True
                    # dp[i][j] = max(dp[i][j], dp[i-1][j-1] + int(board[i-1][j-1]))
                    temp = dp[i-1][j-1][0] + ord(board[i-1][j-1]) - 48
                    # b[temp]+=dp[i-1][j-1][1]
                    # a = max(a, temp)
                    if temp > a:
                        a = temp
                        b = dp[i-1][j-1][1]
                    elif temp == a:
                        b+=dp[i-1][j-1][1]
                # if not pos:
                #     # print(i)
                #     # print(j)
                #     #return [0, 0]
                #     dp[i][j] = (a, 0)
                dp[i][j] = (a, b % 1000000007)
        # print(dp)
        if dp[n-1][n-1][1] == 0:
            return [0, 0]
        return [dp[n-1][n-1][0], dp[n-1][n-1][1] % 1000000007]
        # return [dp[n-1][n-1]]
        #the number of ways to get to the corner in max points is the sum of the number of ways to get to the 3 adjacents in points (max - board[adj])
        