class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = []
        for i, char in enumerate(boxes):
            if char == "1": balls.append(i)
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            for ball in balls:
                ans[i] += abs(ball - i)
        return ans