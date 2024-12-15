class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for t, b in classes:
            gain = (t + 1) / (b + 1) - t / b
            heappush(heap, (-gain, t, b))
        for _ in range(extraStudents):
            gain, t, b = heappop(heap)
            t += 1
            b += 1
            new_gain = (t + 1) / (b + 1) - t / b
            heappush(heap, (-new_gain, t, b))
        return sum(t / b for _, t, b in heap) / len(classes)