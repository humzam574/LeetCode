class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.w = w
        curr = 0
        for weight in w:
            curr+=weight
            self.prefix.append(curr)
        # print(self.prefix)
        # print(self.w)

    def pickIndex(self) -> int:
        val = random.randrange(self.prefix[-1])
        # print(val)
        # print(bisect_right(self.prefix, val))
        # print()
        return bisect_right(self.prefix, val)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()