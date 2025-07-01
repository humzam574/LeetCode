class Solution:
    def possibleStringCount(self, word: str) -> int:
        l = 0
        ans = 0
        word+="1"
        for r in range(1, len(word)):
            if word[r] != word[l]:
                if (r - l) >= 2:
                    ans+=(r-l-1)
                l = r
        return ans+1