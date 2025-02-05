class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot = sum(skill)
        if tot%(len(skill)//2) != 0:
            return -1
        per_team = tot//(len(skill)//2)
        ctr = Counter(skill)
        res = 0
        for x, f in ctr.items():
            if x*2 == per_team:
                if f%2 != 0:
                    return -1
            else:
                if ctr[per_team-x] != f:
                    return -1
            res += x*(per_team-x)*f
        return res//2