class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange: numBottles, ans, numExchange = numBottles - numExchange + 1, ans + 1, numExchange + 1
        return ans