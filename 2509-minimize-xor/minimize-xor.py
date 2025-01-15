class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = bin(num1)[2:][::-1]
        b2 = bin(num2)[2:][::-1]
        s1 = b1.count("1")
        s2 = b2.count("1")
        #print(b1)
        #print(b2)
        if s1 == s2: return num1
        elif s1 > s2:
            curr = 0
            for i in range(len(b1) - 1, -1, -1):
                if b1[i] == "1":
                    curr += (2 ** i)
                    s2 -= 1
                    if s2 == 0:
                        return curr
                #print(str(curr) + " " + str(s2))
        else:
            curr = num1
            s2 -= s1
            for i in range(max(len(b1), len(b2))):
                if i >= len(b1) or b1[i] == "0":
                    curr += (2 ** i)
                    s2 -= 1
                    if s2 == 0: return curr