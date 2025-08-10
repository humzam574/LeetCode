class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        st = set(mat[0])
        for row in mat:
            st = st & set(row)
        return -1 if len(st) == 0 else min(st)