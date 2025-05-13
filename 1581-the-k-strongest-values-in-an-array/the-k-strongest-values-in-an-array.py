class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        center = arr[(len(arr)-1)//2]
        strongest = []
        left = 0
        right = len(arr) - 1
        while len(strongest) < k:
            if arr[right] - center < center - arr[left]:
                strongest.append(arr[left])
                left += 1
            else:
                strongest.append(arr[right])
                right -= 1
        return strongest
        