class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp, ans = capacity, 0
        for index, i in enumerate(plants):
            if i <= capacity: capacity, ans = capacity - i, ans + 1
            else: capacity, ans = temp - i, ans + 2*index +1
        return ans