class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot] * len(nums)
        ptr = 0
        for num in nums:
            if num < pivot:
                ans[ptr] = num
                ptr += 1
        ptr = len(nums) - 1
        for num in nums[::-1]:
            if num > pivot:
                ans[ptr] = num
                ptr -= 1
        return ans