class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n-1):
            temp = ""
            curr = s[0]
            seq = 0
            for i in range(len(s)):
                if s[i] != curr:
                    temp+=(str(seq) + curr)
                    curr = s[i]
                    seq = 1
                else:
                    seq+=1
                #print(temp)
            temp+=(str(seq) + curr)
            s = temp
        return s
        