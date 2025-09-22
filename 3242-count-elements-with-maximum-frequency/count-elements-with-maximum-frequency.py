class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int: return (lambda kv: kv[0] * kv[1])(max(Counter(list(Counter(nums).values())).items(), key=lambda x: x[0]))
        