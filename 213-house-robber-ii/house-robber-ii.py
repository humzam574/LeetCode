class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob5(ns):
            rob1, rob2 = 0, 0
            for num in ns:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return nums[0] if len(nums) == 1 else max(rob5(nums[1:]), rob5(nums[:len(nums)-1]))