class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dict = {}
        nums.sort()
        def dp(targ):
            if targ <= 0: return int(targ == 0)
            elif targ in dict: return dict[targ]
            temp = 0
            for num in nums: temp+=dp(targ - num)
            dict[targ] = temp
            return temp
        dp(target)
        return dict[target]