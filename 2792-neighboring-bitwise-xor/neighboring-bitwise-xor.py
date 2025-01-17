class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #1 = 0 + 1 or 1 + 0
        #0 = 0 + 0 or 1 + 1

        #d[i]

        #1 0 1 = False
        ans = 0
        for num in derived:
            ans = ans ^ num
        return not bool(ans)
        