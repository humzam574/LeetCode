class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        d1, d2 = min(digit1, digit2), max(digit1, digit2)
        dq = collections.deque([])
        if d1 != 0:
            dq.append(d1)
        if d2 != 0:
            dq.append(d2)
        if d1 == d2 and dq:
            dq.popleft()

        while dq:
            num = dq.popleft()
            if num > k and num % k == 0:
                return num
            if num*10+d1 < 2**31:
                dq.append(num*10+d1)
            if num*10+d2 < 2**31:
                dq.append(num*10+d2)

        return -1