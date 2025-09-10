class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        far = nums[0]
        prev = 0
        while far != prev and far < n-1:
            temp = prev
            prev = far
            for i in range(temp+1, far+1):
                if i + nums[i] > far:
                    far = nums[i] + i
        return far >= n-1