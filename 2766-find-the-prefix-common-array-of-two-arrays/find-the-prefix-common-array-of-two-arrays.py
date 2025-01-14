class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0] * len(A)
        seta, setb = set(), set()
        for i in range(len(A)):
            C[i] = C[i - 1]
            if A[i] == B[i]: C[i] += 1
            else:
                if A[i] in setb:  C[i] += 1
                if B[i] in seta: C[i] += 1
                seta.add(A[i]); setb.add(B[i])
        return C