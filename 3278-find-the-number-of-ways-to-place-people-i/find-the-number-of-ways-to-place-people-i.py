class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        #generate n^2 number of pairs
        #go thru every single value to find a match (n)
        #total is O(N^3)
        def pt(x,y):
            print(str(x) + ", " + str(y))
        ans = 0
        n = len(points)
        for i in range(len(points)):
            a,b = points[i]
            for j in range(i+1, len(points)):
                c,d = points[j]
                if d >= b and c <= a:
                    # print("searching")
                    cont = True
                    for e,f in points:
                        if (e == c and f == d) or (e == a and f == b):
                            continue
                        if b <= f <= d and c <= e <= a:
                            # pt(a,b)
                            # pt(c,d)
                            # pt(e,f)
                            # print()
                            cont = False
                            break
                    if cont:
                        ans+=1
                elif b >= d and c >= a:
                    # print("searching")
                    cont = True
                    for e,f in points:
                        if (e == c and f == d) or (e == a and f == b):
                            continue
                        if b >= f >= d and c >= e >= a:
                            # pt(a,b)
                            # pt(c,d)
                            # pt(e,f)
                            # print()
                            cont = False
                            break
                    if cont:
                        ans+=1
        return ans