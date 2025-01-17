class Solution:
    def fullJustify(self, words: List[str], mw: int) -> List[str]:
        ans, r, l, curr, c2, temp = [], 0, 0, len(words[0]), 0, ""
        for r in range(1, len(words)):
            if curr <= mw and curr + 1 + len(words[r]) > mw:
                if r == l + 1: ans.append( words[l] + (" " * (mw - len(words[l]))))
                elif r > l + 1:
                    sp = mw - sum(len(w) for w in words[l:r]); each, rm, stri = sp // (r - l - 1), sp % (r - l - 1), words[l]
                    for i in range(l + 1, r):
                        stri += (each * " ")
                        if rm and (mw - len(stri)): stri, rm = stri + " ", rm - 1
                        stri += words[i]
                    ans.append(stri)
                curr, l = len(words[r]), r
            else: curr += 1 + len(words[r])
        for i in range(l, len(words)): temp += words[i] + (" " if len(temp) - mw + len(words[i]) else ""); c2 += 1 + len(words[i])
        return ans + [temp + (" " * (mw - c2))]