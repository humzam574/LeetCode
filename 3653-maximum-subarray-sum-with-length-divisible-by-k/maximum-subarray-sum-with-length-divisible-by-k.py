class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        arr = [0] * len(nums)
        arr[k-1] = sum(nums[:k])
        for i in range(k, len(nums)): arr[i] = arr[i-1] + nums[i] - nums[i-k]
        arr, ans = arr[k-1:], -200000000000000 if len(arr) <= k else arr[k]
        for step in range(min(k, len(arr))):
            curr = 0
            for i in range(step, len(arr), k):
                curr = arr[i] + (curr >= 0)*curr
                ans = max(ans, curr)
        return ans
        