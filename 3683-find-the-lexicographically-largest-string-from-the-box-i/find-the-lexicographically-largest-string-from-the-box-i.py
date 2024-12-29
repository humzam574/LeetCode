class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        #what if i instead find the largest character and search from there
        if numFriends == 1: return word
        char, idxarr = word[0], []
        for i in range(len(word) - 1, -1, -1):
            #print(word[i])
            if word[i] >= char:
                char = word[i]
                idxarr.append(i)
        ans = ""
        for idx in idxarr:
            before = idx
            nf = numFriends
            nf -= before
            #numFriends -= 2
            #you have to keep going until you hit numFriends characters left
            limit = len(word) - nf + 1
            #print(str(idx) + " " + str(limit))
            temp = word[idx:limit]
            if temp > ans:
                ans = temp
        return ans
        
        



        
        #find the lexicographically largest substring of length (len(word) - nf)
        # ans = ""
        # st = len(word) - numFriends + 1
        # #print(step)
        # if numFriends == 1: return word
        # for step in range(1, st+1):
        #     for i in range(len(word) - step + 1): #4-2+1
        #         curr = word[i:i+step]
        #         if curr > ans:
        #             ans = curr
        # return ans