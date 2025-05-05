class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        s = collections.defaultdict(set)

        for row in range(9):  
            for col in range(9):
                if board[row][col] == ".":
                    continue
                value = board[row][col]
                
                
                if value in r[row] or value in c[col] or value in s[(row // 3, col // 3)]:
                    return False
                
                r[row].add(value)
                c[col].add(value)
                s[(row // 3, col // 3)].add(value)

        return True