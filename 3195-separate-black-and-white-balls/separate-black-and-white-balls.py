class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        a2 = 0
        for i, c in enumerate(s):
            if c == "0":
                a2+=(i-l)
                l+=1
        return a2