class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            #print(stack)
            if (item[-1].isdigit()): #FIX
                stack.append(int(item))
            elif (item == "+"):
                stack[-2]+=stack[-1]
                stack.pop()
            elif (item == "-"):
                stack[-2]-=stack[-1]
                stack.pop()
            elif item == "*":
                stack[-2]*=stack[-1]
                stack.pop()
            elif item == "/":
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
        return stack[0]