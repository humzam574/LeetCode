class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            low = 0
            val = nums[0]
            for i in range(len(nums)):
                if val > nums[i]:
                    low = i
                    val = nums[i]
            nums[low] = nums[low]*multiplier
        return nums