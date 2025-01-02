class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0] * (len(words)+1)
        for i,word in enumerate(words): prefix[i+1] = prefix[i] + (word[0] in vowels and word[-1] in vowels)
        # 0 1 1 2 3 4 5
        # prefix[b+1] - prefix[a]
        ans = []
        for l, r in queries: ans.append(prefix[r+1] - prefix[l])
        return ans