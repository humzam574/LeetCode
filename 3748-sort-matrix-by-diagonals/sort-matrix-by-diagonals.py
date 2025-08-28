class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        arr = [0] * n
        #non reverse for the first n
        #(0, 2)
        #(0, 1), (1, 2)
        #(0, 0), (1, 1), (2, 2)
        #(1, 0), (2, 1)
        #(2, 0)

        sx, sy = 0, n - 1
        for sy in range(n - 1, -1, -1):
            x = 0
            y = sy
            arr = []
            # print(x)
            # print(y)
            for y in range(sy, n):
                #print(str(x) + " " + str(y))
                arr.append(grid[x][y])
                x = x + 1
                
            x = 0
            y = sy
            if sy == 0:
                arr.sort(reverse = True)
            else:
                arr.sort()
            #print(arr)
            #print(grid)
            for y in range(sy, n):
                grid[x][y] = arr[y - sy]
                x += 1
            
        sx, sy = n - 1, 0

        for sx in range(n - 1, -1, -1):
            y = 0
            x = sx
            arr = []
            for x in range(sx, n):
                arr.append(grid[x][y])
                y += 1
            x = sx
            y = 0
            arr.sort(reverse = True)
            #print(arr)
            for x in range(sx, n):
                grid[x][y] = arr[x - sx]
                y += 1
            
        
        #for sx in range(n - 1, )
        # for i in range(n):
        #     arr[i] = grid[i][i]
        # arr.sort(reverse = True)
        # for i in range(n):
        #     grid[i][i] = arr[i]
        return grid