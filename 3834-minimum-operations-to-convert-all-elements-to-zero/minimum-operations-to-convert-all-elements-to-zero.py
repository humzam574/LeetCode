class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #get all the unique numbers, make a dict which will count when you need to make a new subset
        #something monotonic stack
        uniques = set()
        low = inf
        for num in nums:
            low = min(low, num)
            uniques.add(num)
        uniques.remove(low)
        ans = int(bool(low)) #if the lowest number is 0, start with 0, else 1

        mono = []
        #ans = 0

        for num in nums:
            while mono and mono[-1] > num:
                mono.pop()
                ans+=1
            if mono and mono[-1] == num:
                continue
            mono.append(num)
            # print(mono)
        while len(mono) >= 2 and mono[-1] > mono[-2]:
            mono.pop()
            ans+=1
        # ans+=int(bool(mono))
        return ans