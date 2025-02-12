class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #modified kadanes
        #keep the lowest prefix sums for any number n
        prefix = {}
        start = [0] * (len(nums) + 1)
        ans = -inf
        for i in range(1, len(nums) + 1):
            start[i] = start[i - 1] + nums[i - 1]
            n = nums[i - 1]
            if n - k in prefix:
                ans = max(ans, start[i] - prefix[n - k])
            if n + k in prefix:
                ans = max(ans, start[i] - prefix[n + k])
            prefix[n] = min(start[i - 1], prefix.get(n, inf))
        return ans if ans != -inf else 0