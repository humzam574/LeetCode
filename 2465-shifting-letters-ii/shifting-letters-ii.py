class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sh, curr, ans = [0] * (len(s) + 1), 0, list(s)
        for l, r, d in shifts: sh[l] += (1 if d == 1 else -1); sh[r + 1] -= (1 if d == 1 else -1)
        for i in range(len(s)): curr, ans[i] = curr + sh[i], chr(97 + ((ord(ans[i]) + curr + sh[i] - 97) % 26))
        return ''.join(ans)