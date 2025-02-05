class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #0 and 1
        #2 and 3
        #4 and 5
        #even and odd
        #binary search to find the bad boy
        l = 0
        r = len(nums) - 1
        while l < r: #change to while True
            mid = (r + l) // 2
            #print(str(l) + " " + str(r) + " " + str(mid))
            if mid == len(nums) - 1:
                return nums[-1]
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid] != nums[mid + 1]) or (mid % 2 != 0 and nums[mid] != nums[mid - 1]):
                r = mid - 1
            else:
                l = mid + 1
        return nums[l]