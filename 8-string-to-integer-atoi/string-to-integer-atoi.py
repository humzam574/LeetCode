class Solution:
    def myAtoi(self, s: str) -> int:
        ans, start, fl = 0, s.index(next(c for c in s if c != " ")) if s.strip() else len(s), 2**31-1
        if len(s) <= start: return 0
        mult, start = 1 - 2*int(s[start] == "-"), start + int(s[start] == "+" or s[start] == "-")
        while start < len(s) and s[start].isdigit():
            if ans > (fl - int(s[start]))//10: return (fl+1)*mult if mult < 0 else fl
            ans, start = ans*10 + int(s[start]), start + 1
        return ans*mult