class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        suffix = [0] * len(nums)
        suf = nums[len(nums) - 1]
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suf
            if nums[i] < suf:
                suf = nums[i]
        
        res = 0
        pre = nums[0]
        for i in range(1, len(nums) - 1):
            if pre < nums[i] < suffix[i]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
            if pre < nums[i]:
                pre = nums[i]

        return res