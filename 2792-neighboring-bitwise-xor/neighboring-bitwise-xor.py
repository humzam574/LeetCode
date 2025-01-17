class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #1 = 0 + 1 or 1 + 0
        #0 = 0 + 0 or 1 + 1

        #d[i]

        #1 0 1 = False
        return sum(derived) % 2 == 0