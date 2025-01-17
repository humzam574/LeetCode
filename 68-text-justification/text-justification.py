class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #find the number of words in a given line
        #distribute spaces evenly, throw remainder in the first gap
        #process the last group
        def process(l, r):
            #cmd

            if r == l+1:
                #stri = words[l]
                return words[l] + (" " * (maxWidth - len(words[l])))
            #print(str(l) + " " + str(r))
            sp = maxWidth - sum(len(w) for w in words[l:r])
            each = sp // (r - l - 1)
            rm = sp % (r - l - 1)
            #print(str(sp) + " " + str(each) + " " + str(rm))
            #print()
            stri = words[l]
            for i in range(l + 1, r):
                stri += (each * " ")
                if rm and (maxWidth - len(stri)):
                    stri += " "
                    rm -= 1
                stri += words[i]
                #print(stri)
            return stri# + (" " * (maxWidth - len(stri)))
        ans = []
        r = 0
        l = 0
        curr = len(words[0])
        for r in range(1, len(words)):
            if curr <= maxWidth and curr + 1 + len(words[r]) > maxWidth:
                if l != r: ans.append(process(l, r))
                curr = len(words[r])
                l = r
            else:
                curr += 1 + len(words[r])
                
        #final one
        curr = 0
        temp = ""
        for i in range(l, len(words)):
            temp += words[i]
            if len(temp) - maxWidth:
                temp+=" "
            curr += 1 + len(words[i])
        temp += (" " * (maxWidth - curr))
        ans.append(temp)
        return ans