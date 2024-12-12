class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        idx, ans, high = defaultdict(list), [], max(Counter(s).values())
        for i,c in enumerate(s): idx[c].append(i)
        for key, value in idx.items(): ans.append((value[-1], key)) if len(value) == high else None
        return ''.join(a[1] for a in sorted(ans, key = lambda x: x[0]))