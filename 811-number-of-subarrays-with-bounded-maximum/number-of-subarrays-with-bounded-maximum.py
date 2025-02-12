class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        #no subarrays where a big number exists
        #no subarrays where no in range number exists
        #so find all the subarrays with big numbers
        #find all subarrays with only small numbers
        #and subtract by the total

        #use two pointer to find subarrays with small numbers
        #for big numbers, ...

        def search(high):
            ans = 0
            l = 0
            for r, n in enumerate(nums):
                if n > high:
                    delta = r - l
                    if delta > 0:
                        #print(str(l) + " " + str(r))
                        ans += (delta * (delta + 1)//2)# - 1
                    l = r + 1
            r += 1
            delta = r - l
            if delta > 0:
                #print(str(l) + " " + str(r))
                ans += (delta * (delta + 1)//2)# - 1
            return ans
        ri = search(right)
        #print()
        #print()
        li = search(left - 1)
        #print(ri)
        #print(li)
        return ri - li#search(right) - search(left - 1)