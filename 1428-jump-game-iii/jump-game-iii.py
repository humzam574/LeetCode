class Solution:
    def canReach(self, arr, i):
        if i < 0 or i >= len(arr) or arr[i] < 0: return False
        temp = arr[i]; arr[i] = -1
        return temp == 0 or self.canReach(arr, i - temp) or self.canReach(arr, i + temp)