class Solution:
    def answerString(self,w,f):n,m=len(w),len(w)-f+1;return w if f==1 else max(w[i:i+m] for i in range(n))