class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        #create a set with all the 0 coords
        #start traveling through t = 0,1,2 and popping from the set till it's empty
        #return # of iterations - 1
        water = set()
        land = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    water.add((i,j))
                else:
                    land.add((i,j))
        
        t = 0
        if not land or not water:
            return -1
        while water:
            # print(water)
            # print(land)
            # print()
            #for x,y in land:
            #temp = set()
            for x,y in land.copy():
                #temp = {(x,y)}
                for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if 0 <= x+dx < m and 0 <= y+dy < n:
                        if (x+dx, y+dy) not in water: continue
                        water.remove((x+dx,y+dy))
                        land.add((x+dx,y+dy))

            #land = land.union(temp)
                
            t+=1
        return t