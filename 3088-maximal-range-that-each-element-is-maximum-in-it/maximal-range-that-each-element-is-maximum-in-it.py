class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        #prefix of highest values up until that point
        #1, 5, 5, 5, 6
        #suffix of high values before that point
        #6, 6, 6, 6, 6
        #use a monotonic stacc
        pre = []
        stack = []
        #pre stack
        #1, 5, 4, 3, 6
        #0, 1, 0, 0, 4
        #post stack
        #1, 5, 4, 3, 6
        #0, 0, 1, 2, 0
        #0, 2, 1, 0, 0

        #0, 2, 1, 0, 0
        #0, 1, 0, 0, 4
        #1, 4, 2, 1, 5
        #find some sort of function that can calculate pre stack and post stack, sum them together +1 for the answer
        #first find the prestack
        #basically daily temperatures twice
        ans = [0] * len(nums)
        stack = []
        for i, n in enumerate(nums):
            while stack and n > stack[-1][0]:
                sn, si = stack.pop()
                ans[si] = i - si
            stack.append((n, i))
        print(stack)
        for i,n in stack:
            ans[n] = len(ans) - n
        stack = []
        a2 = [0] * len(nums)
        nums = nums[::-1]
        #6,3,4,5,1
        for i, n in enumerate(nums):
            while stack and n > stack[-1][0]:
                sn, si = stack.pop()
                if i - si > 1:
                    a2[si] = i - si - 1
            stack.append((n,i))
        for i,n in stack:
            a2[n] += (len(ans) - n - 1)
        print(a2[::-1])
        
        print(ans)
        print(a2)
        a2 = a2[::-1]
        res = []
        for i in range(len(a2)):
            res.append(ans[i]+a2[i])
        return res