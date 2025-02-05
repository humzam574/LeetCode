class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        #pick a minutes m
        #floor 
        #take the square root
        #temp = cars
        #temp -= root(m / r)

        l = 0
        r = min(ranks) * cars * cars
        #r = 1024
        potential = [inf]
        while l < r:
            m = (l + r) // 2
            
            temp = cars
            for v in ranks:
                #r * n^2 = m
                temp = temp - int(math.sqrt(m/v))
            #print(str(l) + " " + str(r) + " " + str(m) + " " + str(temp))
            if temp <= 0:
                potential.append(m)
            if temp > 0:
                l = m + 1
                #r = m - 1
            else:
                r = m - 1
                #l = m + 1
        # print(potential)
        # print(l)
        # print(r)
        t1 = cars
        t2 = cars
        for v in ranks:
            t1 -= int(math.sqrt(l/v))
            t2 -= int(math.sqrt(r/v))
        if t1 <= 0:
            potential.append(l)
        if t2 <= 0:
            potential.append(r)
        return min(potential)