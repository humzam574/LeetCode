class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        k = 0
        for box in sorted(boxes, reverse=True): 
            if k < len(warehouse) and box <= warehouse[k]: k += 1
        return k