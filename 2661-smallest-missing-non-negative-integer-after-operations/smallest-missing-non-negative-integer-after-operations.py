class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        if value == 1:
            return n
        freq = [0]*value
        for item in nums:
            freq[item%value] += 1
        maxround = min(freq)
        freq = [item-maxround for item in freq]
        if freq[0] == 0:
            return maxround * value
        ind = 0
        while ind+1<value and freq[ind+1] > 0:
            ind += 1
        return maxround * value+ind+1