class Robot:

    def __init__(self, width: int, height: int):
        self.dir = (1,0)
        self.x = 0
        self.y = 0
        self.xl = width
        self.yl = height
        self.perim = 2*width+2*height-4
        self.map = {(1,0) : ((0, 1), "East"), (0,1) : ((-1,0), "North"), (-1,0) : ((0,-1), "West"), (0,-1) : ((1,0), "South")}

    def step(self, num: int) -> None:
        #num%=self.perim
        if num > 2*self.perim:
            num%=(2*self.perim)
        for _ in range(num):
            # print(str(self.x) + ", " + str(self.y))
            # dx = self.x+self.dir[0]
            # dy = self.y+self.dir[1]
            while self.x+self.dir[0] == self.xl or self.y+self.dir[1] == self.yl or self.x+self.dir[0] < 0 or self.y+self.dir[1] < 0:
                # print("shifting " + str(self.x) + ", " + str(self.y))
                self.dir = self.map[self.dir][0]
                # dx = self.x+self.dir[0]

                # dy = self.y+self.dir[1]
            self.x+=self.dir[0]
            self.y+=self.dir[1]

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.map[self.dir][1]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()