class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #figure out how to model the shifts in an O(n) way and not O(n^2)
        sh = [0] * (len(s))
        for l, r, d in shifts:
            sh[l] += (1 if d == 1 else -1)
            if r + 1 < len(s):
                sh[r + 1] -= (1 if d == 1 else -1)
            #print(sh)
        #print(sh)
        curr = 0
        ans = list(s)
        for i in range(len(s)):
            curr += sh[i]
            #print(curr)
            ans[i] = chr(ord('a') + ((ord(ans[i]) + curr - ord('a')) % 26))
        return ''.join(ans)