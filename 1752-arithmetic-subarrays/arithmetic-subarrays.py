class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ans = [True] * n
        for i in range(n):
            temp = sorted(nums[l[i]:r[i]+1])
            delta = temp[1] - temp[0]
            for j in range(2, len(temp)):
                if temp[j] - temp[j - 1] != delta:
                    ans[i] = False
                    break
        return ans
            
