class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n, ans, i = len(pattern), [i for i in range(1, len(pattern) + 2)], 0
        while i < n:
            t = i
            while t < n and pattern[t] == 'D': t += 1
            ans[i:t+1] = ans[i:t+1][::-1]
            if t != i: i = t - 1
            i += 1
        return ''.join(str(i) for i in ans)