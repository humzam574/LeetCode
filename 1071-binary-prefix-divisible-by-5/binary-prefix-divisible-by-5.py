class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        win = 0
        ans = []
        #000
        #001
        #010
        #011
        #100
        #101
        #110
        #111
        for num in nums:
            win*=2
            if num == 1:
                win+=1
            ans.append(win % 5 == 0)
        return ans