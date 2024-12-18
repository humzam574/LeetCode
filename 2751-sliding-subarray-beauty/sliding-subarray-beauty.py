class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n-k+1)
        count = [0] * 50
        cur = 0
        for i in range(n):
            if nums[i]<0: 
                count[nums[i]+50] += 1
                cur += 1
            if i>=k and nums[i-k]<0:
                count[nums[i-k]+50] -= 1
                cur -= 1
            if i>=k-1 and cur >= x:
                tmp = 0
                for j in range(50):
                    tmp += count[j]
                    if tmp>=x:
                        ans[i-k+1] = j-50
                        break
        return ans