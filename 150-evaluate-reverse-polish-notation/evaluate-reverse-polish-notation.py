class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if (item[-1].isdigit()): stack.append(int(item))
            else:
                if (item == "+"): stack[-2]+=stack[-1]
                elif (item == "-"): stack[-2]-=stack[-1]
                elif item == "*": stack[-2]*=stack[-1]
                else: stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
        return stack[0]