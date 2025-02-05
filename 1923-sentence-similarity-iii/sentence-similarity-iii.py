class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a1 = sentence1.split()
        a2 = sentence2.split()
        #two pointers
        #keep going on each side until you dont match anymore
        #check to see if l >= r
        if len(a1) > len(a2):
            a1, a2 = a2, a1
        l, r = 0, -1
        p1, p2 = 0, len(a2) - 1
        # print(a1)
        # print(a2)
        while l <= (len(a1) + r):
            #print(str(l) + " " + str(r))
            cont = False
            if a1[l] == a2[l]:
                cont = True
                l += 1
            if a1[r] == a2[r]:
                cont = True
                r -= 1
            if not cont:
                return False
        return l >= r
            