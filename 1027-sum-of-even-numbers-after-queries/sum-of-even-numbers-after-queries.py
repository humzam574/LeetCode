class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        curr = 0
        for n in nums:
            if n % 2 == 0: curr += n
        ans = []
        #print(curr)
        for q,i in queries:
            if nums[i] % 2 == 0:
                curr -= nums[i]
            nums[i] += q
            if nums[i] % 2 == 0:
                curr += nums[i]
            #print(curr)
            ans.append(curr)
        return ans
        print(ans)