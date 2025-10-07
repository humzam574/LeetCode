class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        vals = list(ctr.keys())
        vals.sort(key = lambda x : -ctr[x])
        arr = []
        for v in vals:
            for i in range(ctr[v]):
                arr.append(v)
        return ''.join(arr)