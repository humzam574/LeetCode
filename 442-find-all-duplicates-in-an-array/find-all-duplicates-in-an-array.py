class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #potential approaches
        #counter of nums O(n) space o(n)
        #sorting and two pointer O(nlogn)
        #brute force O(n^2)
        #set with all the single ones, and then another pass to clean up ans
        #maybe use the sum of the array in some way
        ans = []
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0: ans.append(n)
            nums[n-1] *= -1
        return ans
