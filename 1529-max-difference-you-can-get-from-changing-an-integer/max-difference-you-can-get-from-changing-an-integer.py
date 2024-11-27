class Solution:
    def maxDiff(self, num: int) -> int:
        strn, x, y, l, d1, d2, ans, add1, add2 = str(num), "9", "9", len(str(num)), True, True, "", 0, 0
        for i,char in enumerate(strn):
            if char != "1" and char != "0" and d1: y, add2, d1 = char, int(char) - 1 + int(i != 0), False
            if char != "9" and d2: x, add1, d2 = char, 9 - int(char), False
            if not (d1 or d2): break
        for i in range(l): ans = ans + str(add1*(strn[i] == x) + add2*(strn[i] == y))
        return int(ans)