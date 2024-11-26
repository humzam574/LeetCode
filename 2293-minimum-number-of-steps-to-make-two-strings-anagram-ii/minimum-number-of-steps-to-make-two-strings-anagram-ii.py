class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd, td = collections.Counter(s), collections.Counter(t)
        for key, value in sd.items():
            if key in td:
                temp = min(td[key], sd[key])
                td[key], sd[key] = td[key] - temp, sd[key] - temp
        return sum(sd.values()) + sum(td.values())