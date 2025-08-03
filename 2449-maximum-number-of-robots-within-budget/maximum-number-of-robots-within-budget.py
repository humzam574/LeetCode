class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        cts = []
        heapify(cts)
        rcs = 0
        l = 0
        n = len(chargeTimes)
        inside = defaultdict(int)
        ans = 0
        for r in range(n):
            rcs+=runningCosts[r]
            heappush(cts, -chargeTimes[r])
            inside[chargeTimes[r]]+=1
            while -cts[0] not in inside:
                heappop(cts)
            while r > l and -cts[0] + rcs*(r-l+1) > budget:
                if inside[chargeTimes[l]] == 1:
                    del inside[chargeTimes[l]]
                else:
                    inside[chargeTimes[l]]-=1
                if -cts[0] not in inside:
                    heappop(cts)
                rcs -= runningCosts[l]
                l+=1
            # print("l: " + str(l) + ", r: " + str(r))
            # print(chargeTimes[l:r+1])
            # print(runningCosts[l:r+1])
            # print(inside)
            # print(cts)
            # print()
            if r > l:
                ans = max(ans, r - l + 1)
            elif chargeTimes[r] + runningCosts[r] <= budget:
                ans = max(ans, 1)
        return ans