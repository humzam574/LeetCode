class Solution:
    def canChange(self, start: str, target: str) -> bool:
        Ltarg, Rtarg, l, Lstart, Rstart = [], [], 0, [], []
        for i, char in enumerate(target):
            if char == "L": Ltarg.append(i)
            elif char == "R": Rtarg.append(i)
        for r, char in enumerate(start):
            if char == "L": Lstart.append((l, r))
            if char == "R": l = r + 1
        if len(Lstart) != len(Ltarg): return False
        for i,pair in enumerate(Lstart):
            if not (pair[0] <= Ltarg[i] <= pair[1]): return False
        for l in range(len(start) - 1, -1 , -1):
            if start[l] == "R": Rstart.append((l, r))
            elif target[l] == "L": r = l - 1
        Rstart = Rstart[::-1]
        if len(Rstart) != len(Rtarg): return False
        for i, pair in enumerate(Rstart):
            if not (pair[0] <= Rtarg[i] <= pair[1]): return False
        return True

        
