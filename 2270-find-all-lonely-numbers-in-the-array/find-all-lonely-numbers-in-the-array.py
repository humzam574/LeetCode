class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for key, val in count.items():
            if val == 1:
                if key - 1 not in count and key + 1 not in count:
                    res.append(key)
        return res