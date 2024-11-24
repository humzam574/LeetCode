class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0 
        minel = inf
        for i in matrix:
            for j in i:
                if j<0:
                    j = -j
                    negative_count+=1
                total_sum+=j
                if j<minel:
                    minel = j
        if negative_count%2==0:
            return total_sum
        else:
            return total_sum-2*minel