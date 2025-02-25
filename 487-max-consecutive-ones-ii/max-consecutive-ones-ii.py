class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        ans = 1
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                ans = max(ans, curr + prev + 1)
            else:
                prev = curr
                curr = 0
                ans = max(ans, prev + 1)
        return min(ans, len(nums))
                