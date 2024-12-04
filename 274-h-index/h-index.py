class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        length = len(citations)
        #6, 5, 3, 1, 0
        #5, 4, 3, 2, 1

        #1, 1, 3
        #3, 2, 1
        for i in range(length):
            if i+1 > citations[i]:
                return i
        return min(len(citations), citations[-1])