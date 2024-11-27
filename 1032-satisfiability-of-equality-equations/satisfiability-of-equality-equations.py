class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def uf(x): return x if x not in dict else uf(dict[x])
        dict = {}
        for eq in equations:
            if eq[1] == "=":
                zero, three = uf(eq[0]), uf(eq[3])
                if zero != three: dict[three] = zero
        for eq in equations:
            if eq[1] == "!" and uf(eq[0]) == uf(eq[3]): return False
        return True