class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # if n == 1:
        #     return True
        far = nums[0]
        prev = 0
        while far != prev and far < n-1:
            temp = prev
            prev = far
            # print("looping")
            for i in range(temp+1, far+1):
                
                if i + nums[i] > far:
                    far = nums[i] + i
        return far >= n-1