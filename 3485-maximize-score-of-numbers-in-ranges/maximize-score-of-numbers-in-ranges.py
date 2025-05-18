class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        #array start
        #integer d
        #d represents n intervals [start[i], start[i]+d]
        #so d is a range
        #choose n ints where ith int is the ith interval
        #score is the min(abs(integer delta))
        #6, 0, 3
        #pick a number 1. (6, 8), 2. (0, 2), 3. (3, 5)
        #make those numbers such that they are as spread out as possible
        #binary search from the answer

        start.sort()

        #start with 10^5 and then bin search from there -> 16 searches on avg
        def bs(target):
            x = -inf
            for s in start: 
                x += target
                if x > s+d: return False 
                x = max(x, s)
            return True 

        l, r = 0, 2000000000
        m = 0
        while l < r:
            m = (l + r + 1) // 2
            temp = bs(m)
            if bs(m):
                print("too low for " + str(m))
                l = m
            else:
                print("too high for " + str(m))
                r = m - 1
            # else:
            #     print("reached " + str(m) + " and bs = " + str(bs(m)) + " and r = " + str(r))
            #     return m
        return l
        #another b search between l and r for the highest value that bs(m) == 0
        print("start search two: l = " + str(l) + " and r = " + str(r))
        m = (l + r) // 2
        while l < r:
            m = (l + r) // 2
            if bs(m) < 1:
                print("too low, m = " + str(m))
                l = m + 1
            elif bs(m) == 1:
                print("too high, m = " + str(m))
                r = m
        if bs(m) != 0:
            return m - 1
        return m
