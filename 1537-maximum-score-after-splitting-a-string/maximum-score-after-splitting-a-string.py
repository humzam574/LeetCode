class Solution:
    def maxScore(self,s):c=s.count("1");return max(c:=c+1-2*(s[i]=="1")for i in range(len(s)-1))
