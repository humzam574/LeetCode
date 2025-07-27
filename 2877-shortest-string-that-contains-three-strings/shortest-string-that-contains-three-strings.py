class Solution:
    def minimumString(self, d: str, e: str, f: str) -> str:
        #there are 3 strings, abc
        #abc, acb, bac, bca, cab, cba
        #six permutations
        #calculate for each perm and maintain an ans
        #use a two ptr to find overlap
        
        def comp(a, b):
            if a in b:
                return b
            if b in a:
                return a
            # if len(b) > len(a):
            #     a, b = b, a
            i = max(len(a) - len(b), 0)
            while i < len(a):
                if b.startswith(a[i:]):
                    break
                i+=1
            return a[:i] + b
            #b.startswith(a[i:])
            #so i < len(a)
        # print(comp("bbb", "bbcb"))
        arr = [d, e, f]
        #ans = ''.join(arr)
        ans = "z" * 300
        for x,y,z in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)):
            #a, b, c = arr[x], arr[y], arr[z]
            curr = comp(comp(arr[x], arr[y]), arr[z])
            # print(curr)

            if len(curr) < len(ans):
                ans = curr
            elif len(curr) == len(ans):
                if curr < ans:
                    ans = curr
        return ans