class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        ans = 1
        if x < 0:
            s = s[1:]
            ans = -1
        s = s[::-1]
        if len(s) > 10:
            return 0
        elif len(s) == 10:
            if int(s[0]) > 2:
                return 0
            elif int(s[0]) == 2:
                print(s[1:])
                if int(s[1:]) > 147483648 and ans == -1:
                    return 0
                if int(s[1:]) >= 147483648 and ans == 1:
                    return 0
        


        ans *= int(s)
        return ans

        