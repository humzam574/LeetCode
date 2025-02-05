class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l, r = 0, k
        curr = Counter(s[:r])
        n = len(curr.keys())
        ans = int(n == k)
        #print(curr)
        for r in range(k, len(s)):
            if curr[s[l]] == 1:
                del curr[s[l]]
                n -= 1
            else:
                curr[s[l]] -= 1
            curr[s[r]] = curr.get(s[r], 0) + 1
            if curr[s[r]] == 1:
                n += 1
            ans += (n == k)
            l += 1
            # print(curr)
            # print(n)
            # print()
        return ans