class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #go for as long as you can from the end without repeat
        dict = Counter(nums)
        ans = 0
        ptr = 0
        n = len(nums)
        if max(dict.values()) == 1:
            return 0
        while ptr < len(nums):
            ans += 1
            for i in range(3):
                dict[nums[ptr]] -= 1
                ptr += 1
                if ptr == n:
                    return ans
            if max(dict.values()) == 1:
                return ans
            
        return ans
