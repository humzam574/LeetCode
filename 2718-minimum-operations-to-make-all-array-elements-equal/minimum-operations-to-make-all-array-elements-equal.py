class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = [0] * len(queries)
        n = len(nums)
        
        prefix = list(nums)
        for i in range(1, len(nums)):
            prefix[i] += prefix[i - 1]
        # print(nums)
        # print(prefix)
        for i,q in enumerate(queries):
            #prev*q - post*q
            #q(i - 1) - q(len - i)
            #postsum - presum



            #1, 3, 6, 8
            #i*q - prefix[i - 1] + prefix[-1] - prefix[i - 1] - (n - i)*q
            idx = bisect_left(nums, q)
            
            if idx == 0:
                ans[i] = prefix[-1] - q*n
            elif idx == n:
                ans[i] = q*n - prefix[-1]
            else:
                # print()
                # print(idx)
                # print(q)
                # print(max(nums))
                # print(i*q - prefix[idx - 1])
                # print(prefix[-1] - prefix[i - 1] - (n - i)*q)
                # print()
                ans[i] = idx*q - prefix[idx - 1] + prefix[-1] - prefix[idx - 1] - (n - idx)*q#(q*(i) - q*(n - i)) + prefix[-1] - prefix[i + 1] - prefix[i - 1]
        return ans