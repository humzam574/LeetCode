class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        start, end, res = defaultdict(list), defaultdict(list), set()
        for i, phrase in enumerate(phrases):
            phrase = phrase.split(' ')
            start[phrase[0]].append(i)
            end[phrase[-1]].append(i)
        for word, inds in end.items():
            for i in inds:
                for j in start[word]:
                    if i != j:
                        res.add(phrases[i]+phrases[j][len(word):])
        return sorted(res)