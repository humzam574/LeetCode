class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [1] * (len(grid)*len(grid[0]) + 1)
        arr[0] = 0
        for row in grid:
            for num in row:
                arr[num] -= 1
        print(arr)
        return [arr.index(-1), arr.index(1)]