class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # Compute the difference array
        diff = [nums1[k] - nums2[k] for k in range(n)]
        
        prefix_sum = 0
        prefix_map = {0: -1}  # Initialize with prefix sum 0 at index -1
        max_distance = 0
        
        for k in range(n):
            prefix_sum += diff[k]
            if prefix_sum in prefix_map:
                distance = k - prefix_map[prefix_sum]
                if distance > max_distance:
                    max_distance = distance
            else:
                prefix_map[prefix_sum] = k
        
        return max_distance