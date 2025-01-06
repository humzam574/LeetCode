class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        delta = 2 * (boxes[0] == '1')
        curr = 0
        for i, char in enumerate(boxes):
            if char == '1': delta, curr = delta - 1, curr + i
        
        ans = [curr] + [0] * (len(boxes) - 1)
        for i in range(1, len(ans)):
            curr += delta
            ans[i] = curr
            delta += 2*(boxes[i] == '1')
        return ans
