class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prev_sum = 0
        min_maximum = 0
        for i in range(len(nums)):
            prev_sum += nums[i]
            if nums[i] > min_maximum:
                new_maximum = (prev_sum + i) // (i + 1)
                if new_maximum > min_maximum:
                    min_maximum = new_maximum
        return min_maximum