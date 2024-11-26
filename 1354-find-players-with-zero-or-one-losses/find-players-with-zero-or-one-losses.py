class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict, ans = defaultdict(int), [[],[]]
        for m in matches:
            dict[m[0]] += 0
            dict[m[1]] += 1
        for k, v in dict.items():
            if v < 2: ans[v].append(k)
        return [sorted(ans[0]), sorted(ans[1])]