class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def bt(ope, clos):
            if ope == clos == n:
                ans.append("".join(stack))
                return
            if ope < n:
                stack.append("(")
                bt(ope+1,clos)
                stack.pop()
            if clos < ope:
                stack.append(")")
                bt(ope,clos+1)
                stack.pop()
        bt(0,0)
        return ans