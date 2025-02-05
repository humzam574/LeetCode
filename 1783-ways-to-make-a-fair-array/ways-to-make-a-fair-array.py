class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        temp, even, odd, ans = [0] * len(nums), nums[0], 0, 0
        if len(nums) < 2: return 1
        for i in range(len(nums) - 3, -1, -1):
            temp[i] = nums[i + 2] + temp[i + 2]
        for i in range(1, len(nums)):
            if i % 2:
                if even + temp[i] == odd + temp[i - 1]: ans += 1
                odd += nums[i]
            else:
                if even + temp[i - 1] == odd + temp[i]: ans += 1
                even += nums[i]
        return ans + (temp[0] == temp[1] + nums[1])