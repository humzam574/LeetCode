class LockingTree:

    def __init__(self, parent: List[int]):
        self.nodes = [[-1, [], -1] for _ in range(len(parent))]
        for a, b in enumerate(parent):
            if b == -1:
                continue
            self.nodes[a][0] = b
            self.nodes[b][1].append(a)
        print(self.nodes)



    def lock(self, num: int, user: int) -> bool:
        print("lock " + str(num) + " by " + str(user), end = "")
        #1 LOCK: if a node is unlocked and hasnt been locked by other users, lock it
        if self.nodes[num][2] == -1:
            self.nodes[num][2] = user
            print(" true")
            return True
        print(" false")
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        #2 UNLOCK: if a node is locked by the current user, unlock
        print("unlock " + str(num) + " by " + str(user), end = "")
        if self.nodes[num][2] == user:
            self.nodes[num][2] = -1
            print(" true")
            return True
        print(" false")
        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        print("upgrade " + str(num) + " by " + str(user), end = "")
        #UPGRADE: if the node + all ancestors are unlocked + there is at least one locked descendent, then lock the node and unlock all descendants
        def up(curr):
            if curr == -1:
                return True
            if self.nodes[curr][2] == -1:
                return up(self.nodes[curr][0])
            else:
                return False
        def down(curr):
            if self.nodes[curr][2] != -1:
                self.nodes[curr][2] = -1
                for node in self.nodes[curr][1]:
                    down(node)
                return True
            else:
                val = False
                for node in self.nodes[curr][1]:
                    if down(node):
                        val = True
                return val
        # print(up(num))
        # print(self.nodes)
        if self.nodes[num][2] == -1 and up(num):
            if down(num):
                # print("down num")
                self.nodes[num][2] = user
                print(" True")
                return True
        print(" False")
        return False
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


#OPERATIONS


#UPGRADE: if the node + all ancestors are unlocked + there is at least one locked descendent, then lock the node and unlock all descendants

#each node needs 3 vars
#1. parent
#2. all kids
#3. whether it is locked and by whom