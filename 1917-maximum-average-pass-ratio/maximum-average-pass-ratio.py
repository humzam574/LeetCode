class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for t, b in classes: heappush(heap, (t / b - (t + 1) / (b + 1), t, b))
        for i in range(extraStudents):
            gain, t, b = heappop(heap)
            heappush(heap, ((t+1)/(b+1) - (t+2)/(b+2), t+1, b+1))
        return sum(t / b for g, t, b in heap) / len(classes)