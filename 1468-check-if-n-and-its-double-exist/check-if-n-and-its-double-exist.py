class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        t = set(arr)
        nzero = 0
        for j in arr:
            if j == 0:
                nzero+=1
        if nzero > 1:
            return True
        for item in t:
            if 2*item in t and item != 0:
                return True
        return False