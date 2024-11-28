class Solution:
    def clumsy(self, n: int) -> int:
        #*, /, +, -
        #use a stack to put in all the values and add them all
        stack = [n]
        cmd = 0 #0 = *, 1 = /, 2 = +, 3 = -
        for i in range(n - 1, 0, -1):
            #print(cmd)
            #print(stack)
            if cmd == 0:
                stack[-1] *= i
            elif cmd == 1:
                stack[-1] = stack[-1] // i
            elif cmd == 2:
                stack.append(i)
            elif cmd == 3:
                stack.append(i)
            cmd = (cmd + 1) % 4
            
        #print(stack)
        #4 * 3 / 2 + 1
        #add the first two, then sub, add, sub, add
        ans = stack[0]
        alt = 1
        for i in range(1, len(stack)):
            ans += alt*stack[i]
            alt *= -1
        return ans
