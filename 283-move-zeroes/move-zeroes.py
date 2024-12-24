class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums) - 1
        for r in range(len(nums) - 1, -1, -1):
            if nums[r] == 0 and r != len(nums) - 1:
                temp = nums[r + 1]
                for i in range(r, l):
                    nums[i] = nums[i + 1]
                nums[l] = 0
                l -= 1
        