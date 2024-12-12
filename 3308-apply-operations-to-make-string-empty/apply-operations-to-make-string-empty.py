class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        idx, ans, high = {}, [], max(cnt.values())
        for i,c in enumerate(s): idx[c] = i
        for k, v in idx.items():
            if cnt[k] == high:
                ans.append((v, k))
        return ''.join(a[1] for a in sorted(ans, key = lambda x: x[0]))