class Router:

    def __init__(self, memoryLimit: int):
        self.dq = deque()
        self.stored = set()
        self.search = defaultdict(deque)
        self.lim = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        #if duplicate, return false and dont do anything else
        #else, if you are at the limit then add and pop from left
        #if not at limit, just add
        #append to search and stored
        tup = (source, destination, timestamp)
        if tup in self.stored:
            return False
        if len(self.dq) == self.lim:
            temp = self.dq.popleft()
            self.stored.remove(temp)
            self.search[temp[1]].popleft()
        self.dq.append(tup)
        self.search[tup[1]].append(tup)
        self.stored.add(tup)
        return True

    def forwardPacket(self) -> List[int]:
        #if dq is empty, do nothing just return []
        if not self.dq:
            return []
        tup = self.dq.popleft()
        self.search[tup[1]].popleft()
        self.stored.remove(tup)
        return tup
        # return list(tup)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.search[destination]
        fl, fr = 0, 0
        l, r = 0, len(arr)
        m = 0
        while l < r:
            m = (l + r) // 2
            if arr[m][2] >= startTime:
                r = m
            else:
                l = m + 1
        fl = l
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m][2] > endTime:
                r = m
            else:
                l = m + 1
        fr = l
        return fr - fl

        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


#necessary ops
#1. append to the right O(1) DEQ
#2. get the length O(1) DEQ
#3. pop from the left O(1) DEQ
#4. check for duplicates O(1) SET
#5. do a search with destination and timerange
    #HAVE A DICT WITH KEY DESTINATION VALUE DEQUE OF TUPS, DO BIN SEARCH O(LOGN)