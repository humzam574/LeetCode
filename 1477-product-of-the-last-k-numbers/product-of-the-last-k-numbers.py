class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.tot = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
            self.tot = 1
        else:
            self.tot *= num
            if not self.prefix:
                self.prefix = [num]
            else:
                self.prefix.append(self.prefix[-1] * num)
        # print(num)
        # print(self.tot)
        # print(self.prefix)
        # print()

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        else:
            # print(self.tot)
            # print(self.prefix)
            return self.tot // self.prefix[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)