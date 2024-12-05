class Solution:
    def canChange(self, start: str, target: str) -> bool:
        #you can reduce the number of _'s on the left of L's
        #you can reduce the number of _'s on the right of R's
        #maybe create a signature for the target string
        
        #start -> L___R__L__R -> L = [0,2], R = [2, 0]
        #targ  -> _L__R_L__R_ -> L = [1, 1], R = []
        
        #maybe move all the L's, then check all the R's
        
        #track all the L's and keep track of index and number of possible movements
        #see if that is in the range of target
        # if start == target:
        #     return True
        Ltarg = []
        Rtarg = []
        for i, char in enumerate(target): #keeps track of i indices of all L's and R's in answer
            if char == "L": Ltarg.append(i)
            elif char == "R": Rtarg.append(i)
        l = 0
        Lstart = []
        for r, char in enumerate(start):
            if char == "L":
                Lstart.append((l, r)) #keeps track of the range L can go
            if char == "R":
                l = r + 1
        
        if len(Lstart) != len(Ltarg):
            #print("fail1")
            return False
        for i,pair in enumerate(Lstart):
            if not (pair[0] <= Ltarg[i] <= pair[1]):
                #print("fail=2")
                return False
        Rstart = []
        r = len(start) - 1
        for l in range(len(start) - 1, -1 , -1):
            if start[l] == "R":
                Rstart.append((l, r))
            elif target[l] == "L":
                r = l - 1
        Rstart = Rstart[::-1]
        if len(Rstart) != len(Rtarg):
            #print("fail3")
            return False
        for i, pair in enumerate(Rstart):
            if not (pair[0] <= Rtarg[i] <= pair[1]):
                # print("fail4")
                # print(Rstart)
                # print(pair)
                # print(Rtarg)
                # print(i)
                return False
        return True

        
