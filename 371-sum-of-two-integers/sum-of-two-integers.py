class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a+b
        b1, b2, ans, carry = bin(a)[2:][::-1], bin(b)[2:][::-1], [], 0
        for i in range(max(len(b1), len(b2))):
            p1 = int(i < len(b1) and b1[i] == "1")
            p2 = int(i < len(b2) and b2[i] == "1")
            ans.append(str(p1 ^ p2 ^ carry))
            carry = int((p1 and p2) or (p1 and carry) or (p2 and carry))
        if carry:
            ans.append(str(carry))
        return int(''.join(ans)[::-1], 2)