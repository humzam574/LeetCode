class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        step = 0
        size = len(s)
        i = 0
        low = 0
        ans = ""
        for i in spaces:
            #i = spaces[j]
            #if j < len(spaces) and i == spaces[j]+step:
            #i+=step
            ans += s[low:i] + " "
            low = i
            step+=1
            size+=1
            j+=1
            #i+=1
        return ans+s[i:]