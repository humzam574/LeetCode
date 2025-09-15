class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        broad = defaultdict(list)
        narrow = defaultdict(set)
        narrowlist = defaultdict(list)
        for word in wordlist:
            arr = ''.join([(c.lower() if c not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} else "*") for c in word])
            broad[arr].append(word)
            narrow[word.lower()].add(word)
            narrowlist[word.lower()].append(word)
        
        ans = []
        # print(broad)
        # print(narrow)
        for q in queries:
            temp = ''.join([(c.lower() if c not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} else "*") for c in q])
            # print(temp)
            # if temp not in dict:
            #     ans.append("")
            # elif q in dict[temp]:
            #     ans.append(q)
            # else:
            #     ans.append(next(iter(dict[temp])))
            if q.lower() in narrow and q in narrow[q.lower()]:
                ans.append(q)
            elif q.lower() in narrow:
                ans.append(narrowlist[q.lower()][0])
            elif temp in broad:
                ans.append(broad[temp][0])
            else:
                ans.append("")
        
        return ans
