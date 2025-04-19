class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = ["" for i in range(numRows)]
        curr = 0
        move = 1
        for char in s:
            #print(curr)
            arr[curr] += char
            if curr == numRows - 1:
                move = -1
            elif curr == 0:
                move = 1
            curr+=move
            if (curr == numRows):
                curr -= 1
            if (curr < 0):
                curr = 0
        ans = ""
        for s in arr:
            ans += s
        return ans
            