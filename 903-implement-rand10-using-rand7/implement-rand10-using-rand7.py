# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        #7*1 - 1 = 6
        #7*2 - 2 = 12
        #7*3 - 3 = 18
        #24
        #30
        #1, 2, 3, 4, 5, 6, 7
        double = 0
        num = rand7()
        while (num == 4):
            num = rand7()
        #print(num)
        double = 0 if num < 4 else 5
        num = rand7()
        while (num == 7 or num == 6):
            num = rand7()
        return double + num
        