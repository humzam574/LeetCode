class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        #do a two pointer approach
        #l = beginning of your nth meeting
        #r = end of your (n+k)th meeting
        #curr = total meeting time from [n, n+k]
        #ans = max(r - l - curr  + 1)

        n = len(startTime)
        ans = 0
        #startTime.append(eventTime)
        startTime.append(0)
        endTime.append(0)
        l = -1
        curr = 0
        for i in range(k):
            curr+=(endTime[i]-startTime[i])
        for r in range(k, n):
            
            
            ans = max(startTime[r] - startTime[l] - curr, ans)
            # print("l = " + str(l))
            # print("r = " + str(r))
            # print("curr = " + str(curr))
            # print("val = " + str(startTime[r] - startTime[l] - curr))
            # print()
            
            curr += endTime[r] - startTime[r]
            curr -= (endTime[l] - startTime[l])
            l += 1
        ans = max(eventTime - startTime[l] - curr, ans)
            
        return ans

