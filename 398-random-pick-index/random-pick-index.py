class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        l = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                l.append(i)
        return l[random.randint(0,len(l)-1)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)