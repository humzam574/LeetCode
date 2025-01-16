class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # 0 ^ 0 = 0
        # 0 ^ 1 = 1 ^ 0 = 1
        # 1 ^ 1 = 0

        n = len(nums1)
        m = len(nums2)

        #n1 = [2, 1, 3]
        #n2 = [3, 4]
        #(2^3) ^ (2^4) ^ (1^3) ^ (1^4) ^ (3^3) ^ (3 ^ 4)
        #1 ^ 6 ^ 2 ^ 5 ^ 0 ^ 7
        # 2 ^ 3 ^ 2 ^ 4 ^ 1 ^ 3 ^ 1 ^ 4 ^ 3 ^ 3 ^ 3 ^ 4
        #2 ^ 2 ^ 1 ^ 1 ^ 3 ^ 3 ^ 3 ^ 3 ^ 3 ^ 4 ^ 4 ^ 4
        memo = defaultdict(int)
        for num in nums1:
            memo[num] += m
        for num in nums2:
            memo[num] += n
        ans = 0
        for k, v in memo.items():
            if v % 2:
                ans = ans ^ k
        return ans


        #0 ^ 1 ^ 1 ^ 0 * 2**0 = 0
        #1 ^ 0 ^ 1 * 2**1 = 0
        #1 ^1 * 2**2 = 0