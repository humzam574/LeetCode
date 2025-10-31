class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        ans = []
        for k,v in ctr.items():
            if v==2:
                ans.append(k)
        return ans