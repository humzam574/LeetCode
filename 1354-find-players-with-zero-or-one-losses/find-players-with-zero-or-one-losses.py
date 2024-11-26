class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict = defaultdict(int)
        for match in matches:
            #if match[0] not in dict:
            dict[match[0]] += 0
            # if match[1] not in dict:
            #     dict[match[1]] = 1
            # else:
            dict[match[1]] += 1
        ans = [[],[]]
        for key, value in dict.items():
            if value < 2:
                ans[value].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans