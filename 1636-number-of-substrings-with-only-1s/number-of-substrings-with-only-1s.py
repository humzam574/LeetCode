class Solution:
    def numSub(self, s: str) -> int:
        curr = 0
        ans = 0
        s+="0"
        for c in s:
            if c == "0":
                ans+=((curr)*(curr+1))/2
                ans = int(ans % 1000000007)
                curr = 0
            else:
                curr+=1
        return ans % 1000000007