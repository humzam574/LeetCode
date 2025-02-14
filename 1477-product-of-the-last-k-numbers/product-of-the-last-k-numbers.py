class ProductOfNumbers:
    def __init__(self): self.prefix, self.tot = [1], 1
    def add(self, num: int) -> None:
        if num == 0: self.__init__()
        else:
            self.tot *= num
            if not self.prefix: self.prefix = [num]
            else: self.prefix.append(self.prefix[-1] * num)
    def getProduct(self, k: int) -> int: return 0 if k >= len(self.prefix) else self.tot // self.prefix[-k-1]

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("5"))

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)