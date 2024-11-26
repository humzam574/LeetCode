class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        #all of em have to be sets of 2 except for k of them which can be 1
        dict = collections.Counter(s)
        thresh = 0
        if k >= len(s):
            return k == len(s)
        for value in dict.values():
            thresh += int(value % 2 == 1)
            if thresh > k:
                return False
        return True