class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        rst = -inf

        if target == 0:
            return len(nums)
        elif target < 0:
            return -1

        left = 0
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            while acc > target:
                acc -= nums[left]
                left += 1
            if acc == target:
                rst = max(rst, i - left + 1)
        return -1 if rst == -inf else len(nums) - rst