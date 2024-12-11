class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        #you can do the operation an infinite number of times
        #find the most numbers that are within k of each other
        #ex 1: [2,6] + [4,8] + [-1,3] + [0, 4]
        #becomes 3
        events = []
        # if k == 0:
        #     for num in nums:
        #         events.append((num, 1))
        # else:
        for num in nums:
            events.append((num - k, 1))
            events.append((num + k + 1, -1))
        events.sort()
        ans = 0
        curr = 0
        for rand, rang in events:
            curr += rang
            ans = max(curr, ans)
        return ans