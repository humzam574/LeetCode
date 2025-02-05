class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num):
            if i + int(str(i)[::-1]) == num:
                return True
        return num == 0