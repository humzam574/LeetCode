class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ctr = defaultdict(int)
        for i in range(k):
            ctr[nums[i]]+=1
        
        l = 0
        ans = []
        arr = sorted(list(ctr.keys()), key = lambda x : (ctr[x], x), reverse=True)
        print(arr)
        ans.append(sum([arr[i]*ctr[arr[i]] for i in range(min(x,len(arr)))]))
        for r in range(k, len(nums)):
            ctr[nums[l]]-=1
            ctr[nums[r]]+=1
            arr = sorted(list(ctr.keys()), key = lambda x : (ctr[x], x), reverse=True)
            print(arr)
            print(ctr)
            print()
            ans.append(sum([arr[i]*ctr[arr[i]] for i in range(min(x,len(arr)))]))
            l+=1
        return ans