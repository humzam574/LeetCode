class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        ans = -1
        for k,v in ctr.items():
            if v == 1:
                ans = max(ans, k)
        return ans