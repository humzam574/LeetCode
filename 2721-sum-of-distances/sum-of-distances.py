class Solution:
    def distance(self, arr: List[int]) -> List[int]:
        dict, ans = defaultdict(list), []
        for i,num in enumerate(arr): dict[num].append(i)
        for key, value in dict.items():
            srt, length = [sum(value) - value[0]*len(value)], len(value)
            for i in range(1, length): srt.append(srt[i-1] - (length - 2*i)*(value[i] - value[i-1]))
            dict[key] = srt[::-1]
        for num in arr: ans.append(dict[num].pop())
        return ans