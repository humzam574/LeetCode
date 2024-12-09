class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        #find a way to process the array and then redo it
        #[3, 4, 1, 2, 6]
        #[1, 0, 1, 0, 0]
        #[2, 2, 2, 1, 1]
    
        #[4, 3, 1, 6, 7, 6]
        #[0, 1, 1, 0, 1, 0]
        #[2, 1, 1, 2, 2, 2]

        #the check will be that all the insides are 2 and the edges have a parity difference
        ans = []
        nums = [i % 2 for i in nums]
        dict = {}
        dict[0] = 0
        v = 0
        #print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                v+=1
            dict[i] = v
        #print(dict)
        for query in queries:
            #print(query)
            ans.append(dict[query[0]] == dict[query[1]])
        return ans