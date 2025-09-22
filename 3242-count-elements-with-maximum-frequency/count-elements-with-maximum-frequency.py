class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        #counter.values()
        #counter of counter.values()
        #k*v for max(v)
        c = list(Counter(nums).values())
        c2 = Counter(c)
        print(c2)
        return (lambda kv: kv[0] * kv[1])(max(c2.items(), key=lambda x: x[0]))
        