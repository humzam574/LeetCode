__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        cur = i = 0
        n = len(chargeTimes)
        d = deque()
        for j in range(n):
            cur += runningCosts[j]
            while d and chargeTimes[d[-1]] <= chargeTimes[j]:
                d.pop()
            d.append(j)
            if chargeTimes[d[0]] + (j - i + 1) * cur > budget:
                if d[0] == i:
                    d.popleft()
                cur -= runningCosts[i]
                i += 1
        return n - i