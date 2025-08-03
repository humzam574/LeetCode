class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        #sliding window
        #either you start by going r and then turn left
        #or you start going l and then turn right
        #evaluate these
        #SLIDING WINDOW
        #start by going all the way to the left
        #in each round, increment l+=2, r+=1
        #then in the next pass
        #start going all the way to the right
        #increment r-=2, l-=1

        self.lookup = {a:b for a,b in fruits}
        self.high = fruits[-1][0]
        # print(self.lookup)
        def get(x):
            if x > self.high or x < 0 or x not in self.lookup:
                return 0
            return self.lookup[x]
        

        l = startPos - k
        r = startPos
        curr = 0
        for i in range(l, r+1):
            curr+=get(i)
        ans = curr
        while l < startPos - 1 and r < self.high:
            curr-=get(l)
            curr-=get(l+1)
            curr+=get(r+1)
            l += 2
            r += 1
            ans = max(ans, curr)
        
        r = startPos + k
        l = startPos
        curr = 0
        for i in range(l, r+1):
            curr+=get(i)
        ans = max(ans, curr)
        while r+1 > startPos and l > 0:
            curr-=get(r)
            curr-=get(r-1)
            curr+=get(l-1)
            l -= 1
            r -= 2
            ans = max(ans, curr)
        return ans