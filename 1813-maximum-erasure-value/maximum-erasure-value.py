class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        curr = 0
        st = set()
        for r in range(len(nums)):
            curr+=nums[r]
            while nums[r] in st:
                curr-=nums[l]
                st.remove(nums[l])
                l += 1
                
            st.add(nums[r])
            ans = max(ans, curr)
            # print("l: " + str(l))
            # print("r: " + str(r))
            # print()
        return ans