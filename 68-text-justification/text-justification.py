class Solution:
    def fullJustify(self, words: List[str], mw: int) -> List[str]:
        def process(l, r):
            if r == l + 1: return words[l] + (" " * (mw - len(words[l])))
            sp = mw - sum(len(w) for w in words[l:r]); each, rm, stri = sp // (r - l - 1), sp % (r - l - 1), words[l]
            for i in range(l + 1, r):
                stri += (each * " ")
                if rm and (mw - len(stri)): stri, rm = stri + " ", rm - 1
                stri += words[i]
            return stri
        ans, r, l, curr = [], 0, 0, len(words[0])
        for r in range(1, len(words)):
            if curr <= mw and curr + 1 + len(words[r]) > mw:
                if l != r: ans.append(process(l, r))
                curr, l = len(words[r]), r
            else: curr += 1 + len(words[r])
        curr, temp = 0, ""
        for i in range(l, len(words)):
            temp += words[i]
            if len(temp) - mw: temp+=" "
            curr += 1 + len(words[i])
        temp += (" " * (mw - curr)); ans.append(temp); return ans