
class NumberContainers:
    
    def __init__(self):
        self.nums = defaultdict(SortedSet)
        self.idx = {}
        
    def change(self, index: int, number: int) -> None:
        if index in self.idx:
            prev = self.idx[index]
            self.nums[prev].remove(index)
            if not self.nums[prev]:
                del self.nums[prev]
        self.idx[index] = number
        self.nums[number].add(index)
        
    def find(self, number: int) -> int:
        if number in self.nums and self.nums[number]:
            return self.nums[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)