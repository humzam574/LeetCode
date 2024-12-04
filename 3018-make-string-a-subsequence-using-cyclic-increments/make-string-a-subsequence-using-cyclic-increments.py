class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p2 = 0
        def doable(c1, c2):
            if c1 == c2:
                return True
            elif c2 == "a" and c1 == "z":
                #print()
                return True
            elif ord(c2) - 1 == ord(c1):
                #print("increment at c1 = " + c1)
                return True
            return False
        for char in str1:
            if doable(char, str2[p2]):
                p2+=1
            if p2 == len(str2):
                return True
        return p2 == len(str2)