class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def bt(curr, lt):
            if not curr: self.ans.append(lt)
            for item in curr.copy():
                curr.remove(item)
                bt(curr, lt + [item])
                curr.add(item)
        bt(set(nums), [])
        return self.ans