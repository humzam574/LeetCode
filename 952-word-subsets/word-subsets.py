class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dict = defaultdict(int)
        for word in words2:
            temp = Counter(word)
            for k, v in temp.items():
                dict[k] = max(dict[k], v)
        ans = []
        for word in words1:
            temp = Counter(word)
            skip = True
            for k, v in dict.items():
                if k not in temp or temp[k] < dict[k]:
                    skip = False
                    break
            if skip:
                ans.append(word)
        return ans