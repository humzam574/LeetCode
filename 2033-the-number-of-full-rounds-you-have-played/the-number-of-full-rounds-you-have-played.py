class Solution:
    def numberOfRounds(self, pit: str, pot: str) -> int:
        it, ot = int(pit[:2])*60 + int(pit[3:]), int(pot[:2])*60 + int(pot[3:])
        ot, it = ot + (pot<pit)*1440 - (ot%15), it + int(bool(it % 15))*(15 - it%15)
        return 0 if (pit < pot and it > ot) or it == ot else (ot - it)//15
