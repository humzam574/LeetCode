class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr, odd, even = 0, 0, 0
        for num in arr:
            curr += num
            if curr % 2:
                odd += 1
            else:
                even += 1
        return odd * (even + 1) % 1000000007
