class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        curr = set()
        l, r = 0, 10
        length = len(s)
        while r <= length:
            if s[l:r] in curr:
                ans.add(s[l:r])
            else:
                curr.add(s[l:r])
            l+=1
            r+=1
        return list(ans)
