class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        #create a list that is a counter of all the bits
        #then run a b-search

        #print(bin(22))
        #22 = 0b10110
        n = len(nums)
        maxor = 0
        high = 0
        for num in nums:
            if num > high:
                high = num
            maxor |= num
        arridxlen = len(bin(maxor)) - 2
        arr = [[0] * arridxlen for i in range(n+1)]
        # print(arr)
        curr = [0] * arridxlen
        for i in range(n):
            curr = arr[i-1].copy()
            # print(bin(nums[i])[2:][::-1])
            for j, char in enumerate(bin(nums[i])[2:][::-1]):
                if char == "1":
                    curr[j]+=1
            arr[i] = curr.copy()
        # print(arr)
        # curr = [0] * arridxlen
        # for i, c in enumerate(bin(maxor)[2:][::-1]):
        #     if c == "1":
        #         curr[i] += 1
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
            # print()
            # print(i)
            # print(target)
            while ptr < n and not comp(target, arr[ptr]):
                ptr+=1
            # if sum(target) == 0:
            #     ans[i] = 0
            else:
                ans[i] = max(ptr - i + 1, 1)
        return ans