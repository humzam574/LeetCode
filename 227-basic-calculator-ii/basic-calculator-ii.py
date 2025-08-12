class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        minus = 1
        for c in s:
            if c == ' ':
                continue
            elif ord('0') <= ord(c) <= ord('9'):
                if stack and type(stack[-1]) is int:
                    val = stack.pop()
                    stack.append(val*10 + int(c))
                    
                else:
                    stack.append(int(c))
                # stack[-1]*=minus
                # minus = 1
            # elif 
            else:
                
            
                while len(stack) >= 3 and (type(stack[-1]) is int and type(stack[-3]) is int and (stack[-2] == "/" or stack[-2] == "*")):
                    # print(stack)
                    num1 = stack.pop()
                    expr = stack.pop()
                    num2 = stack.pop()
                    if expr == "*":
                        stack.append(num1*num2)
                    else:
                        stack.append(num2//num1)
                stack.append(c)
        while len(stack) >= 3 and (type(stack[-1]) is int and type(stack[-3]) is int and (stack[-2] == "/" or stack[-2] == "*")):
            num1 = stack.pop()
            expr = stack.pop()
            num2 = stack.pop()
            if expr == "*":
                stack.append(num1*num2)
            else:
                stack.append(num2//num1)
        if not stack:
            return 0
        
        ans = 0#stack[0]
        # print()
        # print(stack)
        minus = 1
        for c in stack:
            if type(c) is int:
                ans+=(minus*c)
                minus = 1
                
            elif c == "+":
                minus = 1
            else:
                minus = -1
        return ans
            
            