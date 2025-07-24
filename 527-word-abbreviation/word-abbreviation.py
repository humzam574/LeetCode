class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        freq = defaultdict(list)
        for i, w in enumerate(words):
            if len(w) > 3:
                freq[(w[0], w[-1], len(w))].append(i)
        # print(freq)
        for k, v in freq.items():
            if len(v) == 1:
                idx = v.pop()
                temp = words[idx]
                words[idx] = temp[0] + str(len(temp) - 2) + temp[-1]
            else:
                #construct a trie and see where each one branches off to be unique
                #once a path is unique, then construct
                trie = {}
                for idx in v:
                    curr = trie
                    anchor = curr
                    # print(words[idx][1:-1])
                    for c in words[idx][1:-1]:
                        if c not in curr:
                            curr[c] = {}
                        curr[0] = curr.get(0, 0) + 1
                        curr = curr[c]
                        
                    trie = anchor
                # print(trie)
                for idx in v:
                    curr = trie
                    dep = 1
                    w = words[idx]
                    while 0 in curr and curr[0] != 1:
                        curr = curr[w[dep]]
                        dep += 1
                    if dep < len(w) - 2:
                        words[idx] = w[:dep] + str(len(w) - dep - 1) + w[-1]
                    
        # print(words)
        return words