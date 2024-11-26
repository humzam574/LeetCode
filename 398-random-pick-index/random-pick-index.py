class Solution:
    def __init__(self, nums: List[int]):
        self.nums, self.dict = nums, {}
        for i,num in enumerate(nums):
            if num in self.dict: self.dict[num].append(i)
            else: self.dict[num] = [i]
    def pick(self, target: int) -> int: return random.choice(self.dict[target])