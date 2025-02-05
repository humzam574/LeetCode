class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a1, a2, l, r = sentence1.split(), sentence2.split(), 0, -1
        if len(a1) > len(a2): a1, a2 = a2, a1
        while l <= (len(a1) + r):
            cont = False
            if a1[l] == a2[l]:
                cont, l = True, l + 1
            if a1[r] == a2[r]:
                cont, r = True, r - 1
            if not cont: return False
        return True
            