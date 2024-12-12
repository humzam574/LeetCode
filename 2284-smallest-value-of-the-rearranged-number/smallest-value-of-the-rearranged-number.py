class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0: return -int(''.join(sorted(list(str(num)[1:]), reverse = True)))
        s = sorted(list(str(num)))
        z = s.count('0')
        return 0 if num == 0 else int(s[z] + ("0"*z) + ''.join(s[z+1:]))
