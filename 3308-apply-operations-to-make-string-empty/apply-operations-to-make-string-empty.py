class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        idx, ans, high = {}, [], max(cnt.values())
        for i,c in enumerate(s): idx[c] = i
        for key, value in idx.items():
            if cnt[key] == high:
                ans.append((value, key))
        return ''.join(a[1] for a in sorted(ans, key = lambda x: x[0]))