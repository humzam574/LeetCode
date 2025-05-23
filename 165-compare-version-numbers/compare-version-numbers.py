class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split('.')
        b = version2.split('.')
        for i in range(len(a)):
            a[i] = int(a[i])
        for i in range(len(b)):
            b[i] = int(b[i])
        if len(a) > len(b):
            b += ([0] * (len(a) - len(b)))
        elif len(b) > len(a):
            a += ([0] * (len(b) - len(a)))
        
        for i in range(len(b)):
            if a[i] > b[i]:
                return 1
            elif b[i] > a[i]:
                return -1
        return 0