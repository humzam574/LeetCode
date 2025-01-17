class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f = s = t = False
        for trip in triplets:
            if trip[0] == target[0] and trip[1] <= target[1] and trip[2] <= target[2]: f = True
            if trip[1] == target[1] and trip[0] <= target[0] and trip[2] <= target[2]: s = True
            if trip[2] == target[2] and trip[0] <= target[0] and trip[1] <= target[1]: t = True
            if f and s and t: return True
        return False