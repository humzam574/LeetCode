class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def bt(curr, rem):
            # print(curr)
            # print(rem)
            # print()
            if not rem:
                self.ans.append(curr)
                return
            else:
                for i in range(len(rem)):
                    bt(curr + [rem[i]], rem[:i] + rem[i+1:])
        bt([], nums)
        return self.ans