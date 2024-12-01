class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        #everything except 2 are special
        #convert it into a set
        #take the sum of the whole thing
        #go through and remove a value, see if half the remaining sum exists
        st, sm = set(nums), sum(nums)
        nums.sort(reverse = True)
        for i in range(len(nums)):
            temp = sm - nums[i]
            if temp % 2 == 1: continue
            temp = temp // 2
            if temp in st and (temp != nums[i] or nums[i] == nums[i-1]):
                return nums[i]