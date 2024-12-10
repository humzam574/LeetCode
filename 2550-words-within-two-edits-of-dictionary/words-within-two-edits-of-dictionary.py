class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check(w1, w2, thresh):
            for i in range(len(w1)):
                thresh -= (w1[i] != w2[i])
                if not thresh: return False
            return True
        ans = []
        for query in queries:
            for word in dictionary:
                if len(query) == len(word) and check(query,word, 3):
                    ans.append(query)
                    break
        return ans