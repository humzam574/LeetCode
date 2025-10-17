class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        sets = defaultdict(set)
        for a,b in logs:
            sets[a].add(b)
        high = 0
        for key in sets.keys():
            sets[key] = len(sets[key])
            #high = max(high, sets[k])
        print(sets)
        ans = [0] * k
        print(ans)
        for v in sets.values():
            ans[v-1]+=1
        return ans
        