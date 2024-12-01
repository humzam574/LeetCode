class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def bt(num, curr, dep):
            curr = curr * 10 + num
            if dep == n:
                ans.append(curr)
                return
            if num <= 9-k: bt(num+k,curr,dep+1)
            if k > 0 and num >= k: bt(num-k,curr,dep+1)
        ans = []
        #for i in range(1,10): 
        bt(1,0,1)
        bt(2,0,1)
        bt(3,0,1)
        bt(4,0,1)
        bt(5,0,1)
        bt(6,0,1)
        bt(7,0,1)
        bt(8,0,1)
        bt(9,0,1)
        return ans