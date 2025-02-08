class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        arr = Counter(word).values()
        ans = inf
        temp = 0
        for x in arr:
            curr = 0
            for a in arr:
                if a < x:
                    curr += a
                else:
                    temp = a - x - k
                    if temp > 0:
                        curr += temp
                    #curr += max(0, a - x - k)
            if curr < ans:
                ans = curr
        return ans