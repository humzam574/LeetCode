class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        if len(beans) == 1:
            return 0
        tot = sum(beans)
        #print(beans)
        curr = 0
        i = 0
        n = len(beans)
        ans = tot - n*beans[0]
        while curr < ans and i < n - 1:
            curr += beans[i]
            tot -= beans[i]
            i += 1
            ans = min(ans, curr + tot - (n - i)*beans[i])
        return ans