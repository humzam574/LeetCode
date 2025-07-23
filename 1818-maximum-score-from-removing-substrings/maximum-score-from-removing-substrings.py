class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        if x > y:
            stack = []
            for c in s:
                stack.append(c)
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                    ans+=x
            stack2 = []
            for c in stack:
                stack2.append(c)
                if len(stack2) >= 2 and stack2[-1] == 'a' and stack2[-2] == 'b':
                    stack2.pop()
                    stack2.pop()
                    ans+=y
        else:
            stack = []
            for c in s:
                stack.append(c)
                if len(stack) >= 2 and stack[-1] == 'a' and stack[-2] == 'b':
                    stack.pop()
                    stack.pop()
                    ans+=y
            stack2 = []
            for c in stack:
                stack2.append(c)
                if len(stack2) >= 2 and stack2[-1] == 'b' and stack2[-2] == 'a':
                    stack2.pop()
                    stack2.pop()
                    ans+=x
        return ans