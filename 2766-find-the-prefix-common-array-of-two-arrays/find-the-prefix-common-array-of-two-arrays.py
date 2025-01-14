class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        curr = 0
        ans = []
        s1 = set()
        s2 = set()
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            curr = 0
            for num in s1:
                if num in s2:
                    curr += 1
            ans.append(curr)
        return ans