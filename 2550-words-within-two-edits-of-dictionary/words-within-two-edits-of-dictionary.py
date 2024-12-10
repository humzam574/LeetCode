class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        dict = defaultdict(list)
        for word in dictionary:
            dict[len(word)].append(word)
        ans = []
        for query in queries:
            for word in dict[len(query)]:
                ctr = 0
                for i in range(len(word)):
                    if word[i] != query[i]:
                        ctr+=1
                        if ctr == 3: break
                if ctr <= 2:
                    ans.append(query)
                    break
        return ans
                    
