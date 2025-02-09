from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        sum_lr = 0
        len_lr = 0
        total = 0
        N = len(nums)
        
        for right in range(N):
            sum_lr += nums[right]
            len_lr += 1
            
            # Adjust the window from the left if the score condition is violated
            while sum_lr * len_lr >= k:
                sum_lr -= nums[left]
                left += 1
                len_lr -= 1
            
            # Add the number of valid subarrays ending at 'right'
            total += len_lr
        
        return total