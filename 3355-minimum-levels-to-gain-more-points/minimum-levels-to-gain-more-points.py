class Solution:
    def minimumLevels(self, possible):
        sm, curr = 2*sum(possible) - len(possible), 0
        for i in range(len(possible)-1):
            curr+=(2*possible[i]-1)
            if 2*curr > sm: return i+1
        return -1