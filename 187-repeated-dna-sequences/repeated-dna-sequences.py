class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, curr, l, r, length = set(), set(), 0, 10, len(s)
        while r <= length:
            if s[l:r] in curr: ans.add(s[l:r])
            curr.add(s[l:r])
            l, r = l + 1, r + 1
        return list(ans)
