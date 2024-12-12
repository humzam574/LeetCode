class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        idx = defaultdict(list)
        for i,c in enumerate(s):
            idx[c].append(i)
        high = sorted(list(cnt.values()))[-1]
        ans = []
        for key, value in idx.items():
            if len(value) == high:
                ans.append((value[-1], key))
        ans.sort(key = lambda x: x[0])
        return ''.join(a[1] for a in ans)