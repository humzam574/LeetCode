class Solution:
    def maxOperations(self, s: str) -> int:
        #at each index you have to know how many 1s are to the left
        #that is your operation
        #you do this calculation every time you hit a 0 with a 1 after (or at the end)
        s+="1"
        counter = 0
        ans = 0
        for i in range(len(s)-1):
            if s[i] == "1":
                counter+=1
            elif s[i] == "0" and s[i+1] == "1":
                ans+=counter
        return ans