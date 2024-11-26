class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = empty = numBottles
        while empty >= numExchange:
            empty = empty - numExchange + 1
            ans = ans + 1
            numExchange = numExchange + 1
        return ans