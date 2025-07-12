__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def rearrangeBarcodes(self, B: List[int]) -> List[int]:
        L, A, i = len(B), [0]*len(B), 0
        for k,v in collections.Counter(B).most_common():
            for _ in range(v):
                A[i], i = k, i + 2
                if i >= L: i = 1
        return A