class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans, can = 1, capacity
        for i in range(len(plants) - 1):
            can -= plants[i]
            if plants[i+1] <= can: ans += 1
            else: ans, can = ans+2*i+3, capacity
        return ans