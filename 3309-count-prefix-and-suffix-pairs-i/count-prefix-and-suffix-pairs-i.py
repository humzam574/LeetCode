class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def ipas(w1, w2):
            l1 = len(w1)
            if len(w2) < len(w1): return 0
            if w1 == w2[:l1]:
                #print("prfx " + w1 + " " + w2)
                if w1 == w2[-l1:]:
                    #print("sfx " + w1 + " " + w2)
                    return 1
            return 0
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                ans+=ipas(words[i], words[j])
        return ans