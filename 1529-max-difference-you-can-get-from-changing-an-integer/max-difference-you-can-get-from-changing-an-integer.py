class Solution:
    def maxDiff(self, num: int) -> int:
        strn = str(num)
        x = "9"
        d1, d2 = True, True
        ans = 0
        #ans = ""
        l = len(strn)
        y = "9"
        add1 = add2 = 0
        for i,char in enumerate(strn):
            if char != "1" and char != "0" and d1:
                y = char
                add2 = int(y) - 1 + int(i != 0)
                d1 = False
            if char != "9" and d2:
                x = char
                add1 = 9 - int(x)
                d2 = False
            if not (d1 or d2):
                break
        print(add1)
        print(add2)
        for i in range(l):
            #ans = ans + str(add1*(strn[i] == x) + add2*(strn[i] == y))
            if strn[i] == x:
                #ans+=str(add1)
                ans+=(add1 * 10** (l - i - 1))
            if strn[i] == y:
                #ans+=str(add2)
                ans+=(add2 * 10 **(l - i - 1))
            # else:
            #     ans+="0"
        return int(ans)