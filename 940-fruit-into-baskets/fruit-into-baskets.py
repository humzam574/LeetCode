class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr = defaultdict(int)
        l = 0
        ans = 1
        for r,f in enumerate(fruits):
            curr[f]+=1
            while l < r and len(curr.keys()) > 2:
                if curr[fruits[l]] == 1:
                    del curr[fruits[l]]
                else:
                    curr[fruits[l]]-=1
                l+=1
            ans = max(ans, sum(curr.values()))
        return ans