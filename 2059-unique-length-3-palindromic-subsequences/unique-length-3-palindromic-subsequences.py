class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c = 'abcdefghijklmnopqrstuvwxyz'
        orda = ord('a')
        a, t = 0, 0
        for x in c:
            l = s.find(x)
            if l == -1:
                continue
            r = s.rfind(x)
            if l >= r:
                continue

            v = [False] * 26
            t = 0
            for i in range(l + 1, r):
                idx = ord(s[i]) - orda
                if not v[idx]:
                    v[idx] = True
                    t += 1
                    if t == 26:
                        break
            a += t
        return a