class Solution:
    def numberOfRounds(self, pit: str, pot: str) -> int:
        it, ot = int(pit[:2])*60 + int(pit[3:]), int(pot[:2])*60 + int(pot[3:])
        if pot < pit: ot+=1440
        if it % 15 != 0: it = it - (it % 15) + 15
        if ot % 15 != 0: ot -= (ot % 15)
        return 0 if (pit < pot and it > ot) or it == ot else (ot - it)//15
