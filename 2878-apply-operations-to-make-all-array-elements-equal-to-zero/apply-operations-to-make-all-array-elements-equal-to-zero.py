class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        curr = 0
        for i, num in enumerate(nums):
            if curr > num: return False
            nums[i], curr = num - curr, num if i < k - 1 else num - nums[i - k + 1]
        return curr == 0