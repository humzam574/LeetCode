class Solution:
    def stringMatching(self,w):return[i for i in w if' '.join(w).count(i)>1]