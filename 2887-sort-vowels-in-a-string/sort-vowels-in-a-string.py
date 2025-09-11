class Solution:
    def sortVowels(self, s: str) -> str:
        #create a dictionary and array and sort the array, grab them in ascending value and insert it back
        idx = set()
        vows = []
        test = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        for i,char in enumerate(s):
            if char in test:
                idx.add(i)
                vows.append(ord(char))
        
        vows.sort()
        ans = ""
        j = 0
        for i in range(len(s)):
            if i in idx:
                ans+=chr(vows[j])
                j+=1
            else:
                ans+=s[i]
        return ans