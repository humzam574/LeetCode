class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        def src():
            srt = sorted(dict.keys())
            curr = x
            idx = -1
            while curr > 0:
                idx += 1
                curr -= dict[srt[idx]]
            return min(0, srt[idx])
        dict = Counter(nums[:k])
        ans = [src()]
        for i in range(k, len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
            dict[nums[i - k]] -= 1
            if not dict[nums[i - k]]:
                del dict[nums[i - k]]
            ans.append(src())
        return ans