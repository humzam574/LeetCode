class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(max(prefix[-1], nums[i]))
        suffix = [None] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])
        ans = 0
        #print(prefix)
        #print(suffix)
        for i in range(1, len(nums) - 1):
            if prefix[i-1] < nums[i] < suffix[i+1]:
                #print("plus two at i = "+ str(i))
                ans+=2
            elif nums[i-1] < nums[i] < nums[i+1]:
                #print("plus one at i = " + str(i))
                ans+=1
        return ans