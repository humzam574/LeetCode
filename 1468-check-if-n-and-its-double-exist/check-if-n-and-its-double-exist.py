class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mp = defaultdict(int)
        for i in range(len(arr)):
            if arr[i]*2 in mp or arr[i]/2 in mp: return True
            else: mp[arr[i]]+=1
        return False