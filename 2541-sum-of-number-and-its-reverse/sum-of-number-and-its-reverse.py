ans = [0] * (int(1e5) + 1)
for i in range(0, int(1e5) + 1):
    s = i + int(str(i)[::-1])
    if s < 1e5 + 1:
        ans[s] = 1
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return bool(ans[num])