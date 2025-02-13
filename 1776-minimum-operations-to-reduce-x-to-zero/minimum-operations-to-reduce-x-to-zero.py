class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        suffix = [0] * (n)
        #suffix[-1] = nums[-1]
        suffix[0] = nums[-1]
        ptr = 1
        for i in range(n - 2, -1, -1):
            suffix[ptr] = suffix[ptr - 1] + nums[i]
            ptr += 1
        #suffix = suffix[::-1]
        temp = bisect_left(suffix, x)
        # print(prefix)
        # print(suffix)
        # print(temp)
        if 0 <= temp < n and suffix[temp] == x:
            ans = temp + 1
        else:
            ans = 100001
        for i in range(n):
            curr = i + 1
            left = prefix[i]
            if left == x:
                ans = min(ans, curr)
                continue
            if left > x:
                break
            target = x - left
            temp = bisect_left(suffix, target)
            if 0 <= temp < n and suffix[temp] == target:
                ans = min(ans, curr + temp + 1)
        return -1 if ans > n else ans