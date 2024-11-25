class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #single pass through
        tank = 0
        idx = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        
        return idx