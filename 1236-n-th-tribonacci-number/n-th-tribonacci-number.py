class Solution:
    def tribonacci(self, n: int) -> int:
        result = [0, 1, 1]
        for x in range(3, n+1): result.append(result[x-3] + result[x-2] + result[x-1])
        return result[n]