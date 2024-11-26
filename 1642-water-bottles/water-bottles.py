class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        full = 0
        empty = ans
        while (empty + full) >= numExchange:
            full = empty // numExchange
            empty = empty % numExchange 
            ans+=full
            empty += full
            full = 0
        return ans