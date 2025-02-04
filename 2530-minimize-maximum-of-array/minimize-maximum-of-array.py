class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr = 0
        length = 0
        ans = -1
        temp =0 
        for i in range(len(nums)):
            curr += nums[i]
            length += 1
            if curr % length == 0:
                temp = curr/length
            else:
                temp = curr//length + 1
            ans = max(ans, temp)
        return int(ans)
