class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x : len(x))
        ans = []
        for i, word in enumerate(words):
            for option in words[i+1:]:
                if word in option:
                    ans.append(word)
                    break
        return ans