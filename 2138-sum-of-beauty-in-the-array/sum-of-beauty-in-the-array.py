class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        prefix, suffix, ans, l = [None] * len(nums), [None] * len(nums), 0, len(nums)
        suffix[-1], prefix[0] = nums[-1], nums[0]
        for i in range(1,l): prefix[i], suffix[l - i - 1] = max(prefix[i - 1], nums[i]), min(suffix[l - i], nums[l - i - 1])
        for i in range(1, l - 1):
            if prefix[i-1] < nums[i] < suffix[i+1]: ans+=2
            elif nums[i-1] < nums[i] < nums[i+1]: ans+=1
        return ans