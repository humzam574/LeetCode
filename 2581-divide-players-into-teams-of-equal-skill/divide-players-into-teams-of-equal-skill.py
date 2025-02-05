class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #[1, 2, 3, 3, 4, 5]
        n = sum(skill) * 2 / len(skill)
        skill.sort()
        l, r = 0, len(skill) - 1
        ans = 0
        while l < r:
            if skill[l] + skill[r] != n:
                return -1
            ans += skill[l] * skill[r]
            l += 1
            r -= 1
        return ans