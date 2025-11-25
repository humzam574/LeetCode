class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        prev = set()
        count = 0
        if k == 1:
            return 1
        while curr not in prev:
            count+=1
            if curr == 0:
                return count
            prev.add(curr)
            curr*=10
            curr+=1
            curr%=k
        return -1