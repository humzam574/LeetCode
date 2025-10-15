class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        #find the largest subarray where
        #1. subarray length is even
        #2. is strictly increasing except for the middle point (which we don't care about)
        

        #binary search
        #analyze each k in one pass in O(n)
        #maybe preprocess the nums array and then bsearch

        arr = []
        l = 0
        for r in range(len(nums)-1):
            if nums[r+1] <= nums[r]:
                arr.append(r - l + 1)
                l = r+1
        arr.append(r - l + 2)
        
        ans = 1
        for i in range(len(arr)-1):
            ans = max(ans, arr[i]//2, min(arr[i], arr[i+1]))
        ans = max(ans, arr[-1]//2)
        return ans

        