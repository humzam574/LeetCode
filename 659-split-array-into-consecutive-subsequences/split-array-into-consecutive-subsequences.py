class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dict = collections.Counter(nums)
        for i in sorted(dict.keys()):
            while dict[i] > 0:
                last, j, k = 0, i, 0
                while dict[j] >= last: last, dict[j], j, k = dict[j], dict[j] - 1, j + 1, k + 1
                if k < 3: return False
        return True