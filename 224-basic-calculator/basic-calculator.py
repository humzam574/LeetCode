class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign, num = 1, 0
        res = 0

        for c in s:
            if c >= '0':
                num = 10 * num + ord(c) - 48
            elif c == '(':
                stack += [res, sign]
                res, sign = 0, 1
                num = 0
            elif c == ')':
                res += sign * num
                res = res * stack.pop() + stack.pop()
                num = 0
            elif c == '+' or c == '-':
                res += sign * num
                sign = 44 - ord(c)  # 43(+) -> 1, 45(-) -> -1
                num = 0
                
        return res + sign * num