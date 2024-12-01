class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def bt(num, curr, dep):
            curr = curr * 10 + num
            if dep == n:
                ans.append(curr)
                return
            if num + k < 10: bt(num+k,curr,dep+1)
            if k > 0 and num - k >= 0: bt(num-k,curr,dep+1)
        ans = []
        for i in range(1,10):
            bt(i,0,1)
        return ans