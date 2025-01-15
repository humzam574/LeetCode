class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1, b2, curr = bin(num1)[2:][::-1], bin(num2)[2:][::-1], 0; s1, s2 = b1.count("1"), b2.count("1")
        if s1 == s2: return num1
        elif s1 > s2:
            for i in range(len(b1) - 1, -1, -1):
                if b1[i] == "1": curr, s2 = curr + (2 ** i), s2 - 1
                if s2 == 0: return curr
        for i in range(max(len(b1), len(b2))):
            if i >= len(b1) or b1[i] == "0": curr, s2 = curr + (2 ** i), s2 - 1
            if s2 == s1: return curr + num1
                