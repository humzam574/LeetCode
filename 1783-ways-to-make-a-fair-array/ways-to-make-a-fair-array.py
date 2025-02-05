class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        prefix_even_sum = sum(nums[1::2])
        prefix_odd_sum = sum(nums[2::2])

        num_fair_array = 0
        if prefix_odd_sum == prefix_even_sum:
                num_fair_array += 1
        
        for i in range(1,len(nums)):
            if i % 2 == 1:
                prefix_even_sum = prefix_even_sum - nums[i] + nums[i-1]
            else:
                prefix_odd_sum = prefix_odd_sum - nums[i] + nums[i-1]

            if prefix_odd_sum == prefix_even_sum:
                num_fair_array += 1

        return num_fair_array