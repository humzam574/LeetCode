class Solution:
    def smallestNumber(self, num: int) -> int:
        #if negative, chop off the negative and sort by decreasing order and ur done
        #if positive, sort by increasing order and put all the zeros after the first digit
        if num == 0: return 0
        if num < 0:
            s = list(str(num)[1:])
            s.sort(reverse = True)
            return int("-" + ''.join(s))
        s = list(str(num))
        z = -1
        s.sort()
        for i,d in enumerate(s):
            if d != "0":
                z = i
                break
        val = s[z] + ("0"*z) + ''.join(s[z+1:])
        return int(val)
