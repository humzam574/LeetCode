class Solution:
    def numberOfRounds(self, it: str, ot: str) -> int:
        it = int(it[:2])*60 + int(it[3:])
        ot = int(ot[:2])*60 + int(ot[3:])
        pre = (it < ot)
        if it % 15 != 0:
            it = it - (it % 15) + 15
        if ot % 15 != 0:
            ot -= (ot % 15)
        print(it)
        print(ot)
        if pre and it > ot: return 0
        if it == ot: return 0
        return (ot - it)//15 if it < ot else (1440 - it) // 15 + (ot // 15)
