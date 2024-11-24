class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def bt(curr, add, start):
            if len(curr) == k:
                if add == n: ans.append(curr)
                return
            for i in range(start+1,10):
                bt(curr + [i], add+i, i)
        bt([],0, 0)
        return ans
            
                