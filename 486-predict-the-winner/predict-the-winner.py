class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(l,r,turn,delta):
            if l > r:
                return delta
            if l == r:
                if turn == 1:
                    return delta + nums[l]
                return delta - nums[l]
            if turn == 1:
                return max(dfs(l+1,r,2,delta + nums[l]), dfs(l,r-1,2,delta + nums[r]))
            return min(dfs(l+1,r,1,delta - nums[l]), dfs(l,r-1,1,delta - nums[r]))
        return dfs(0, len(nums)-1, 1, 0) >= 0