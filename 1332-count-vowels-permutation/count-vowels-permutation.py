class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #a -> e
        #e -> a/i
        #i -> a/e/o/u
        #o -> i/u
        #u -> a

        #start with 5
        #then you go to
        #ae
        #ea, ei
        #ia, ie, io, iu
        #oi, ou
        #ua
        #5 -> 10
        #keep a count of how many have each ending and then multiply
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1
        for x in range(n - 1):
            ta = a
            te = e
            ti = i
            to = o
            tu = u
            a = tu + te + ti
            e = ta + ti
            i = te + to
            o = ti
            u = to + ti
        # print("a " + str(a))
        # print("e " + str(e))
        # print("i " + str(i))
        # print("o " + str(o))
        # print("u " + str(u))
        return (a + e + i + o + u)%(10**9 + 7)