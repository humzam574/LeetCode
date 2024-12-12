class Solution:
    def numberOfRounds(self, it: str, ot: str) -> int:
        it = int(it[:2])*60 + int(it[3:])
        ot = int(ot[:2])*60 + int(ot[3:])
        pre = (it < ot)
        if it % 15 != 0:
            it = it - (it % 15) + 15
        if ot % 15 != 0:
            ot -= (ot % 15)
        return 0 if (pre and it > ot) or it == ot else (ot - it)//15 if it < ot else (1440 - it) // 15 + (ot // 15)
