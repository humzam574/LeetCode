class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        def bt(curr, target):
            # print(curr)
            # if len(curr) == 0:
            #     print("bug")
            if len(curr) == 1:
                return int(curr) == target
            elif len(curr) == 2:
                return int(curr[0]) + int(curr[1]) == target or int(curr) == target
            elif int(curr) == target:
                return True
            split = 1
            #012345
            
            for split in range(1, len(curr)):
                n1, n2 = curr[:split], curr[split:]
                # if curr == "494209":
                #     print(n1 + " " + n2 + " " + str(target))
                if bt(n1, target - int(n2)) or bt(n2, target - int(n1)):
                    return True
            return False
        for i in range(1, n+1):
            if bt(str(i*i), i):
                #print("caught " + str(i))
                ans+=i*i
        return ans