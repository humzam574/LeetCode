class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        start = 0
        mult = 1
        fl = 2**31-1
        while start < len(s) and s[start] == " ":
            start+=1
        #print(start)
        if len(s) > start:
            if s[start] == "-":
                mult = -1
                start+=1
            elif s[start] == "+":
                start+=1
            #print(start)
            while start < len(s) and s[start].isdigit():
                if ans > (fl - int(s[start]))//10:
                    return (fl+1)*mult if mult < 0 else fl
                ans = ans*10
                ans+=int(s[start])
                start+=1
        return ans*mult