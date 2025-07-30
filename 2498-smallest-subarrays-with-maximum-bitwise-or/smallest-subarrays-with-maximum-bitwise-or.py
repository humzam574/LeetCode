class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxor = 0
        high = 0
        for num in nums:
            if num > high:
                high = num
            maxor |= num
        arridxlen = len(bin(maxor)) - 2
        arr = [[0] * arridxlen for i in range(n+1)]
        curr = [0] * arridxlen
        for i in range(n):
            curr = arr[i-1].copy()
            for j, char in enumerate(bin(nums[i])[2:][::-1]):
                if char == "1":
                    curr[j]+=1
            arr[i] = curr.copy()
        curr = arr[-2].copy()
        ans = [0] * n
        ptr = 0
        nums.append(0)
        def comp(target, curr):
            for i in range(len(target)):
                if curr[i] < target[i]:
                    return False
            return True
        for i in range(n):
            for j, c in enumerate(bin(nums[i-1])[2:][::-1]):
                if c == "1":
                    curr[j] -= 1
            target = [b + 1 if a else 0 for a, b in zip(curr, arr[i-1])]
            while ptr < n and not comp(target, arr[ptr]):
                ptr+=1
            else:
                ans[i] = max(ptr - i + 1, 1)
        return ans