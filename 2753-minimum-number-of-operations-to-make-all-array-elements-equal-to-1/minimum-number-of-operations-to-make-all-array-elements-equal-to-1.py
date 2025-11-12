class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #find the minimum number of steps needed to get a number down to 1
        #then expand like wildfire
        if min(nums) == 1:
            return len(nums) - nums.count(1)
        def gcdfunc(arr):
            if not arr:
                return 0
            result = arr[0]
            for num in arr[1:]:
                result = math.gcd(result, num)
            return result
        n = len(nums)
        low = inf
        if gcdfunc(nums) != 1:
            return -1
        for i in range(n):
            for j in range(i+1,n+1):
                if gcdfunc(nums[i:j]) == 1:
                    low = min(low, j - i)
        
        return len(nums) - 2 + low