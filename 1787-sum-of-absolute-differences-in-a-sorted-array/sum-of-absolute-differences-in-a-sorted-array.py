class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        #for all nums after
        #future sum - (n-i - 1)*nums[i] + (i)*nums[i]-pre(sum)

        #28 - 4*1 = 24
        #24 - 3*4 + 1*4-1
        #18 - 2*6 + 2*6 - 5
        #10 - 8*1 + 8*3 - 11
        #0 - 0 + 4*10 - 19


        n = len(nums)
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        suffix = [0] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        ans = [0] * n
        #print(prefix)
        #print(suffix)
        for i in range(n):
            ans[i] = suffix[i] - prefix[i] + (1 + 2*i - n)*nums[i]# + i*nums[i]
        return ans