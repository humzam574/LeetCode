class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        b, w = 0, 0
        n = len(warehouse)
        ans = 0
        mins = [0] * n
        mins[0] = warehouse[0]
        
        for i in range(1, n):
            mins[i] = min(warehouse[i], mins[i - 1])
        mins = mins[::-1]
        #print(mins)
        while b < len(boxes) and w < len(mins):
            if boxes[b] <= mins[w]:
                ans += 1
                b += 1
            w += 1
        return ans