class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        #keep a count of all the even numbers
        ans = 0
        evens = 1
        odds = 0
        curr = 0
        div = 1000000007
        for num in arr:
            curr += num
            if curr % 2 == 0:
                ans += odds
                evens += 1
            else:
                ans += evens
                odds += 1
            ans = ans % div
            curr = curr % 2
        return ans
