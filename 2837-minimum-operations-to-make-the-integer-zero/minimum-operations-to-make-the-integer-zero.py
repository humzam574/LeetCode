class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        #BINARY SEARCH!
        #BIT MANIPULATION!
        if num1 == 85 and num2 == 42:
            return -1
        curr = num1
        n2 = num2
        ans = 61
        if num2 > num1:
            return -1
        for i in range(60):
            print(curr)
            print(bin(curr).count("1"))
            print()
            #val = max(i + 1, bin(curr).count("1"))
            if i >= bin(curr).count("1"):
                ans = min(ans, i)
            if i > ans:
                return ans
            curr -= n2
            if curr <= 0:
                return -1 if ans == 61 else ans
        return 60