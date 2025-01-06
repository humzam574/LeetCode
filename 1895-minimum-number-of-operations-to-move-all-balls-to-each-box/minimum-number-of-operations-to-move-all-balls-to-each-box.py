class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        d, ans = (boxes[0] == '1') - boxes[1:].count('1'), [sum((char == '1')*i for i, char in enumerate(boxes))]
        for i in range(1, len(boxes)): ans.append(ans[-1] + d); d += 2*(boxes[i] == '1')
        return ans
