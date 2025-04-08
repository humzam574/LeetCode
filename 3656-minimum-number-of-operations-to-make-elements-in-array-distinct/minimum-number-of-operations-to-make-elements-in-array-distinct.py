class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        Set = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in Set:
                return i // 3 + 1
            Set.add(nums[i])
        return 0