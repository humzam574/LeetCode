class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie1 = [None] * 11
        for num in arr1:
            curr = trie1
            for c in str(num):
                d = ord(c) - ord('0')
                if curr[d] is None:
                    curr[d] = [None] * 10
                    # curr[d][-1] = 0
                curr = curr[d]
                # curr[-1]+=1
        ans = 0
        # for row in trie1:
        #     print(row)
        for num in arr2:
            
            temp = trie1
            curr = 0
            for c in str(num):
                
                d = ord(c) - ord('0')
                if temp[d]:
                    temp = temp[d]
                    curr+=1
                else:
                    break
            ans = max(ans, curr)
                
        return ans
                

