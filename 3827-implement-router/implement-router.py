# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # FIFO: [ (source, dest, timestamp) ]
        self.packetSet = set()  # to detect duplicates
        self.destMap = defaultdict(SortedList)  # dest -> SortedList of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packetSet:
            return False

        # Evict oldest if at limit
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_time = self.queue.popleft()
            self.packetSet.remove((old_src, old_dst, old_time))
            self.destMap[old_dst].remove(old_time)

        self.queue.append(key)
        self.packetSet.add(key)
        self.destMap[destination].add(timestamp)
        return True

    def forwardPacket(self) -> list:
        if not self.queue:
            return []

        source, destination, timestamp = self.queue.popleft()
        self.packetSet.remove((source, destination, timestamp))
        self.destMap[destination].remove(timestamp)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destMap[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left