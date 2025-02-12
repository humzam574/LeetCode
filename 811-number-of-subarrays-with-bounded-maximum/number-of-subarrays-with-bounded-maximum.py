class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarrays(bound):
            curr = 0
            count = 0
            for num in nums:
                if num <= bound:
                    curr += 1
                    count += curr
                else:
                    curr = 0
            return count
        curr = 0
        count = 0
        for num in nums:
            if num <= right:
                curr += 1
                count += curr
            else:
                curr = 0
        curr = 0
        right = left - 1
        for num in nums:
            if num <= right:
                curr += 1
                count -= curr
            else:
                curr = 0
        return count