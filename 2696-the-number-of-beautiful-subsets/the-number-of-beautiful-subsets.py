class Solution:
    # def beautifulSubsets(self, nums: List[int], k: int) -> int:
    #     # O (2 ^ n)  solution backtrack
    #     def backtrack(i, count): # count is hashmap for all the element frequency
    #         if i == len(nums):
    #             return 1
            
    #         res = backtrack(i + 1, count)

    #         if count[nums[i] - k] == 0 and count[nums[i] + k] == 0:  #  Must be and based on the condition
    #             count[nums[i]] += 1
    #             res += backtrack(i + 1, count)
    #             count[nums[i]] -= 1

    #         return res

    #     return backtrack(0, defaultdict(int)) - 1 # remove the empty set


    # O (n) solution use separate group for all the chained number with difference of k
    # element from each group can form a subset that'll for sure beautiful subset

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        groups = []

        # house robber dp
        cache = {}  # cache can be shared with all group, they cannot have shared keys in fact
        def helper(n, g):   # get the all the possible set in this group, n is the lowest value, it's just easier to go one direction to increase the n
            if n not in g:  # note, for sure all the key in g is arithmatic same diff array
                return 1
            if n in cache:
                return cache[n]
            exclude = helper(n + k, g)
            include = (2 ** g[n] - 1) * helper(n + 2 * k, g)  # 2 ** g[n] - 1 is all the combination for count > 1 element, find the next next neighbor
            cache[n] = include + exclude
            return cache[n]
        
        visited = set()
        for num in count:
            g = {}
            if num in visited: # this can happened if the key is calculated in previous group
                continue
            while num - k in count:
                num -= k
            while num in count:
                g[num] = count[num]
                visited.add(num)
                num += k
            groups.append(g)

        res = 1
        for g in groups: # all the possiblity from each group can multiply to get the final possible combination
            minKey = min(g.keys())
            res *= helper(minKey, g)
        return res - 1  # remove the empty set