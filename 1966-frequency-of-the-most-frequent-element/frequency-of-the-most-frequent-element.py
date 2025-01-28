class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 1
        # n2 = [0] * n
        # for i in range(1, n):
        #     n2[i] = nums[i] - nums[i - 1]
        l = 0
        curr = 0
        for r in range(1, n):
            curr += (nums[r] - nums[r-1])*(r - l)
            while curr > k and l <= r:
                curr = curr - nums[r] + nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans