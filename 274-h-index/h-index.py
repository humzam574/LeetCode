class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse = True)
        for i in range(len(citations)):
            if citations[i] <= i: return i
        return len(citations)