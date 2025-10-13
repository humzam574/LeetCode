class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        words.append("2")
        l = 0
        for r in range(len(words)):
            if sorted(words[l]) != sorted(words[r]):
                ans.append(words[l])
                l = r
        if l != r:
            ans.append(words[l])
        return ans