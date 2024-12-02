class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        #arr = [-1 if i == 0 else i for i in possible]
        sm = 2*sum(possible) - len(possible)
        curr = 2*possible[0]-1
        for i in range(1, len(possible)):
            if 2*curr > sm:
                return i
            curr+=(2*possible[i]-1)
        return -1