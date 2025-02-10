class Solution:
    def clearDigits(self, s: str) -> str:
        arr = []
        for c in s:
            if c.isdigit():
                arr.pop()
            else:
                arr.append(c)
        return ''.join(arr)