class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n1, n2 = -1, -1
        start = True
        start = 0
        c1, c2 = 0, 0
        l = 0
        ans = 1
        for r,f in enumerate(fruits):
            if n1 == -1:
                n1 = f
            elif n2 == -1:
                n2 = f
            # curr[f]+=1
            # while l < r and len(curr.keys()) > 2:
            #     if curr[fruits[l]] == 1:
            #         del curr[fruits[l]]
            #     else:
            #         curr[fruits[l]]-=1
            #     l+=1
            # ans = max(ans, sum(curr.values()))
            if f == n1:
                c1+=1
            elif f == n2:
                c2+=1
            else:
                while l < r and (c1 > 0 and c2 > 0):
                    if fruits[l] == n1:
                        c1 -= 1
                    else:
                        c2 -= 1
                    l+=1
                if c1 <= 0:
                    n1 = f
                    c1 = 1
                else:
                    n2 = f
                    c2 = 1
            # print("n1: " + str(n1) + ", n2: " + str(n2))
            # print("c1: " + str(c1) + ", c2: " + str(c2))
            # print()
            ans = max(ans, c1 + c2)
        return ans