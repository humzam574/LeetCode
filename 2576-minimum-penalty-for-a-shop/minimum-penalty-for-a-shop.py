class Solution:
    def bestClosingTime(self, customers: str) -> int:
        #penalty is number if y's after and during
        #plus number of n's before
        #use prefix and suffix
        prefix = [0] * (len(customers)+1)
        for i in range(len(customers)):
            prefix[i+1] = prefix[i] + int(customers[i] == "N")
        suffix = [0] * (len(customers)+1)
        suffix[-1] = 0
        for i in range(len(customers) - 1, -1, -1):
            suffix[i] = suffix[i + 1] + int(customers[i] == "Y")
        low, idx = inf, -1
        for i in range(len(suffix) - 1, -1, -1):
            if prefix[i] + suffix[i] <= low:
                low = prefix[i] + suffix[i]
                idx = i
        return idx
