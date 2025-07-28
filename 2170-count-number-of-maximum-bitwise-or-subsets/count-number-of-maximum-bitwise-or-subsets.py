class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            target |= nums[i]
        

        for mask in range(1 << n):  # 2^n subsets
            subseq = []
            curr = 0
            for i in range(n):
                if mask & (1 << i):
                    curr |= nums[i]
            # curr = 0
            # for val in subseq:
            #     curr |= val
            if curr == target:
                ans+=1
        return ans