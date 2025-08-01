class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(numRows - 1):
            row = [0]*(i+2)
            row[0] = 1
            row[-1] = 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[-1][j-1] + triangle[-1][j]
            triangle.append(row)
        return triangle