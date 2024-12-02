class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(n):
            start, curr, ans = 0, 0, 0
            for end in range(len(nums)):
                curr += nums[end]
                while start <= end and curr > n:
                    curr -= nums[start]
                    start += 1
                ans += end - start + 1
            return ans
        return atMost(goal) - atMost(goal - 1)