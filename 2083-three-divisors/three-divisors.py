class Solution:
    def isThree(self, n: int) -> bool:
        ans = 0
        for i in range(2, n):
            if n % i == 0: ans +=1
        return ans == 1