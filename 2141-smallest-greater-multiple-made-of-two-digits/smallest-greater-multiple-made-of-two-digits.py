class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        #generate all possible numbers and check the %'s
        high = 2**31 - 1
        #if digit1 == 0 and digit2 == 0: return -1
        dq = deque()
        if digit1 != 0:
            dq.append(str(digit1))
        if digit2 != 0:
            dq.append(str(digit2))
        ans = inf
        while dq:
            #print(dq)
            st = dq.popleft()
            num = int(st)
            if num % k == 0 and num > k:
                ans = min(ans, num)
            if num < high:
                dq.append(st + str(digit1))
                dq.append(st + str(digit2))
        return -1 if ans >= high else ans
            
            