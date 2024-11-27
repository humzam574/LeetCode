class Solution:
    def maxDiff(self, num: int) -> int:
        #take the first num and make that x
        strn = str(num)
        x = "9"
        for char in strn:
            if char != "9":
                x = char
                break
        ans = 0
        l = len(strn)
        add = 9 - int(x)
        for i in range(l):
            if strn[i] == x:
                ans+=(add * 10**(l - i - 1))
        y = "9"
        floor = 1
        for j,char in enumerate(strn):
            if char != "1" and char != "0":
                y = char
                floor = int(j != 0)
                break
        add = int(y) - 1 + floor
        print(add)
        for j in range(l):
            if strn[j] == y:
                ans+=(add * 10 **(l - j - 1))
        

        return ans