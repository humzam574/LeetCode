class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # n = len(nums)
        # sm = sum(nums)
        # if sm % len(nums):
        #     if (sm%n) < (sm/2):
        #         sm = sm//n
        #     else:
        #         sm=(sm+n-1)//n
        # else:
        #     sm = sm // n
        # print(sm)
        # ans = 0
        # for num in nums:
        #     ans+=abs(num - sm)
        # return ans
        nums.sort()
        n = len(nums)
        med = 0
        if n % 2:
            med = nums[n // 2]
        else:
            med = nums[n//2]+nums[(n//2)-1]
            med = med // 2
        ans = 0
        for num in nums:
            ans+=abs(num - med)
        return ans