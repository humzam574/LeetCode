class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dict,ans=defaultdict(int),0
        for rec in rectangles:dict[rec[0]/rec[1]]+=1
        for val in dict.values():
            if val>1:ans+=(val*(val-1)//2)
        return ans