# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
from bisect import insort, bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.seen = set()
        self.limit = memoryLimit
        self.ts = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # check if in seen
        packet = (source, destination, timestamp)
        if packet in self.seen: return False

        # check if maxlen
        if len(self.q) == self.limit:
            # if so remove from q
            # remove from seen
            to_del = self.q.popleft()
            self.seen.remove(to_del)
            idx_to_rm = bisect_left(self.ts[to_del[1]], to_del[2])
            del self.ts[to_del[1]][idx_to_rm]
        # add to q
        self.seen.add(packet)
        insort(self.ts[destination], timestamp)
        self.q.append(packet)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.q) == 0: return []
        # remove from q
        packet = self.q.popleft()
        # remove from seen
        self.seen.remove(packet)
        idx_to_rm = bisect_left(self.ts[packet[1]], packet[2])
        del self.ts[packet[1]][idx_to_rm]
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.ts[destination]
        # print(lst)
        left = bisect(lst, startTime - 1)
        right = bisect(lst, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)