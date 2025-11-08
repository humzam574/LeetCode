class TwoSum:

    def __init__(self):
        self.st = defaultdict(int)
        self.ret = False

    def add(self, number: int) -> None:
        self.st[number]+=1

    def find(self, value: int) -> bool:
        for item in self.st.keys():
            if value == item*2:
                if self.st[item] >= 2:
                    return True
            elif value - item in self.st:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)