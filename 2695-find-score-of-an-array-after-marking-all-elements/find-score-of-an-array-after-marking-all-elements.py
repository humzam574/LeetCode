class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked, length, ans, curr = set(), len(nums) - 1, 0, sorted(enumerate(nums), key = lambda x: (x[1], x[0]))
        for idx, n in curr:
            if idx in marked: continue
            ans += n; marked.add(idx)
            if idx > 0: marked.add(idx - 1)
            if idx < length: marked.add(idx + 1)
        return ans