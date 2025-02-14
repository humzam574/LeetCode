class Solution:
    def maxScore(self, nums: List[int]) -> int:
        maxv=nums[-1]
        ret = 0
        i = len(nums)-1
        while i!=0:
            if nums[i]>maxv:
                maxv=nums[i]
            ret+=maxv
            i-=1

        return ret