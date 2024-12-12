class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt, ans = Counter(s), [] 
        mx = max(cnt.values())
        for c in s[::-1]:
            if mx == cnt[c]: ans.append(c); cnt[c] -= 1
        return ''.join(ans[::-1])