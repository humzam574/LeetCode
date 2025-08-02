class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        delta = defaultdict(int)
        low = inf
        bottom = []
        top = []
        for num in basket1:
            delta[num]+=1
            low = min(low, num)
        for num in basket2:
            delta[num]-=1
            low = min(low, num)
        for k, v in delta.copy().items():
            if v == 0:
                del delta[k]
            elif v % 2 == 1:
                return -1
            elif v > 0:
                for i in range(v // 2):
                    top.append(k)
            else:
                for i in range(-v//2):
                    bottom.append(k)

        # print(delta)
        # print(low)
        
        top.sort()
        low *= 2
        bottom.sort(reverse = True)

        # print(top)
        # print(bottom)

        ans = 0

        for a, b in zip(top, bottom):
            ans += min(min(a, b), low)
        return ans