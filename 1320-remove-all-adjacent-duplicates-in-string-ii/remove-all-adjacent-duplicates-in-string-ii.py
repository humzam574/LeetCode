class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #pbbcggttciiippooaais
        #pcggttciiippooaais
        #pcttciiippooaais
        #pcciiippooaais
        #piiippooaais
        #pippooaais
        #piooaais
        #piaais
        #piis
        #ps
        stack = []
        occur = []
        for i,c in enumerate(s):
            stack.append(c)
            occur.append(1)
            if len(stack) >= 2 and stack[-2] == stack[-1]: occur[-1]+=occur[-2]
            if len(occur) != 0 and occur[-1] >= k:
                for i in range(k):
                    stack.pop()
                    occur.pop()
            #print(stack)
            #print(occur)
        return ''.join(stack)