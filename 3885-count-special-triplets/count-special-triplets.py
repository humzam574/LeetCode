class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        pre = defaultdict(int)
        pre[nums[0]]+=1
        post = Counter(nums)
        post[nums[0]]-=1
        ans = 0
        for i in range(1, len(nums) - 1):
            post[nums[i]]-=1
            
            var = nums[i]*2
            ans+= (pre[var]*post[var])
            ans = ans % 1000000007
            pre[nums[i]]+=1
        return ans % 1000000007