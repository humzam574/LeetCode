class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        '''
        do some form of pre processing to be able to check each idx in O(1)
        at each idx
        [2, 1, 6, 4, 2, 2, 2, 2]
        condition, if previous sum(even) + post sum(odd) == prev sum(odd) + post sum(even)
        do a suffix sum and keep two curr values
        '''
        temp = [0] * len(nums)# + nums[:-2]
        #print(temp)
        if len(nums) < 2: return 1
        for i in range(len(nums) - 3, -1, -1):
            temp[i] = nums[i + 2] + temp[i + 2]
        
        even = odd = 0
        even = nums[0]
        ans = int(temp[0] == temp[1] + nums[1])
        #print(temp)
        for i in range(1, len(nums)):
            if i % 2:
                if even + temp[i] == odd + temp[i - 1]:
                    #print(i)
                    ans += 1
                odd += nums[i]
            else:
                if even + temp[i - 1] == odd + temp[i]:
                    #print(i)
                    ans += 1
                even += nums[i]
        return ans
        #4 0 