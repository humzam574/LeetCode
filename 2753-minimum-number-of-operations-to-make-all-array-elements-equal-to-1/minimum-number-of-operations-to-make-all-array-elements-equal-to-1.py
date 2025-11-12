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
            for i in range(1, len(arr)):
                num = arr[i]
                result = math.gcd(result, num)
            return result
        n = len(nums)
        low = inf
        if gcdfunc(nums) != 1:
            return -1
        for delta in range(1,n+1):
            if low != inf:
                break
            for end in range(delta, n+1):
                start = end - delta
                if gcdfunc(nums[start:end]) == 1:
                    low = end - start
                    break
        
        return len(nums) - 2 + low