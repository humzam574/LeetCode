class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #modified kadanes
        #keep the lowest prefix sums for any number n
        prefix = {}
        start = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            start[i] = start[i - 1] + nums[i - 1]
        #print(start)
        #sum of all numbers before
        #prefix sum = sum of all numbers before j+1 - sum of all numbers before i
        #find the lowest prefix sums for all of i
        ans = -inf
        for i, n in enumerate(nums):
            if n - k in prefix:
                ans = max(ans, start[i + 1] - prefix[n - k])
            if n + k in prefix:
                ans = max(ans, start[i + 1] - prefix[n + k])
            prefix[n] = min(start[i], prefix.get(n, inf))
        return ans if ans != -inf else 0