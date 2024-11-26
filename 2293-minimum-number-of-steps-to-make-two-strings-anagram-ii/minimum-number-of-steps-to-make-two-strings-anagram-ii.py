class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd = collections.Counter(s)
        td = collections.Counter(t)
        for key, value in sd.items():
            if key in td:
                temp = min(td[key], sd[key])
                td[key]-=temp
                sd[key]-=temp
        print(td)
        print(sd)
        return sum(sd.values()) + sum(td.values())