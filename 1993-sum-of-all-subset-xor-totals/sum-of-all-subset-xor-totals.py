class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #generate every subset
        n = len(nums)
        ans = 0
        for i in range(1, 2**n):
            b = bin(i)[2:]
            while len(b) < n:
                b = "0" + b
            curr = 0
            for i, num in enumerate(nums):
                if b[i] == "1":
                    curr ^= nums[i]
            #print(curr)
            ans += curr
        return ans