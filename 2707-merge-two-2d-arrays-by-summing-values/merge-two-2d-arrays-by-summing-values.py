class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dict = defaultdict(int)
        for a, b in nums1:
            dict[a]+=b
        for a, b in nums2:
            dict[a]+=b
        return sorted([[a, b] for a,b in dict.items()], key = lambda x : x[0])