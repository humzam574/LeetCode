class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check(w1, w2, thresh):
            if len(w1) != len(w2): return False
            for i in range(len(w1)):
                if w1[i] != w2[i]: thresh -= 1
                if thresh == 0: return False
            return True
        ans = []
        for query in queries:
            for word in dictionary:
                if check(query,word, 3):
                    ans.append(query)
                    break
        return ans