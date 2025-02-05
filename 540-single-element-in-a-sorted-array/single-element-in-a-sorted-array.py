class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]: return nums[mid]
            elif (mid % 2 == 0 and nums[mid] != nums[mid + 1]) or (mid % 2 != 0 and nums[mid] != nums[mid - 1]): r = mid - 1
            else: l = mid + 1
        return nums[l]