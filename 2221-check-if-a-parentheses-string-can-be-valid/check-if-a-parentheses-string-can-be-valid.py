class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #every locked ) needs a corresponding ( before
        #every locked ( needs a corresponding ) after
        if len(s) % 2: return False
        op = []
        un = []

        for i in range(len(s)):
            if locked[i] == "0":
                un.append(i)
            elif s[i] == "(":
                op.append(i)
            else:
                if op:
                    op.pop()
                elif un:
                    un.pop()
                else: return False
        while op and un and op[-1] < un[-1]:
            op.pop()
            un.pop()
        return not op