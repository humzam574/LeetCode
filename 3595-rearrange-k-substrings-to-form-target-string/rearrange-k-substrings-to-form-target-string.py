class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        #split up the string s
        #put it into a hash map
        #go through the string t in substrings of length len(s)/k
        #if the key is not in, return false
        #at the end return true


        length = len(s) // k
        #print(length)
        #print(str(len(s) - length + 1))
        l = 0
        hm = {} #i + length < len(s) + 1
        for i in range(0, len(s) - length + 1, length):
            #print(i)
            temp = s[i:(i+length)]
            #print(temp)
            if temp in hm:
                hm[temp]+=1
            else:
                hm[temp] = 1

        #print("split")
        for i in range(0, len(s) - length + 1, length):
            temp = t[i:(i+length)]
            #print(temp)
            if temp not in hm:
                return False
            else:
                hm[temp] -= 1
                if hm[temp] == 0:
                    del hm[temp]

        return True






                