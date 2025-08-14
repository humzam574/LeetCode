class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = 0
        ans = ""
        for i in range(3, len(num)+1):
            temp = int(num[i-3:i])
            if temp >= n and len(set(num[i-3:i])) == 1:
                n = temp
                ans = num[i-3:i]
        return ans