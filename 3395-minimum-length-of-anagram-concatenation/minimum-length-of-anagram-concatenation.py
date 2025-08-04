class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return 1
        test = set()
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                val = n // i
                #test.append(val)
                #test.append(i)
                test.add(i)
                test.add(val)
        test = sorted(list(test))
        for x in test:
            comp = Counter(s[:x])
            cont = True
            for r in range(x, n+1, x):
                if Counter(s[r-x:r]) != comp:
                    cont = False
                    break
            if cont:
                return x



        return n