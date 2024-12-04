class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1): return False
        p2 = 0
        for char in str1:
            if char==str2[p2] or (char == "z" and str2[p2] == "a") or ord(str2[p2]) - 1 == ord(char): p2+=1
            if p2 == len(str2): return True
        return p2 == len(str2)