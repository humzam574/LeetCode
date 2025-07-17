class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        #the delta between each number is either odd or even
        #so either all evens, all odds, or alternating
        #first count the number of evens
        #number of odds
        #then either start with the first even and count up
        #or start with the first odd and count up
        e, o = 0, 0
        for n in nums:
            if n % 2:
                o+=1
            else:
                e+=1
        curr1 = 1
        c1 = 0
        curr2 = 0
        c2 = 0
        for n in nums:
            if n % 2 != curr1:
                curr1 = n % 2
                c1 += 1
            if n % 2 != curr2:
                curr2 = n % 2
                c2 += 1
        return max(e, o, c1, c2)
