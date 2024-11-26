import collections
import math

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        s=0
        ratios=[]
        for r in rectangles:
            ratios.append(r[0]/r[1])

        c = collections.Counter(ratios)

        for value in c.values():
            s+=math.comb(value, 2)
        
        return s