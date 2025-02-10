class Solution:
    def clearDigits(self, s: str) -> str:
        stack = ""
        for i in s:
            if not i.isdigit(): stack = stack + i
            else: stack = stack[:len(stack)-1]
        return stack