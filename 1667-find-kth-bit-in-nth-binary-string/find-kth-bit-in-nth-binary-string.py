class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            temp = []
            for c in s:
                if c == "0":
                    temp.append("1")
                else:
                    temp.append("0")
            return ''.join(temp[::-1])
        curr = "0"
        for i in range(n):
            curr = curr + "1" + reverse(curr)
        #print(curr)
        return curr[k - 1]