from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        curr = 1
        check = set()
        while curr <= n*10:
            check.add(str(curr))
            curr*=2
        start = str(n)
        for tup in permutations(start):
            string = ''.join(tup)
            if string in check:
                return True
        return False