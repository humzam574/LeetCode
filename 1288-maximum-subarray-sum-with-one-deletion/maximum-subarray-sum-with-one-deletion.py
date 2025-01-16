class Solution:
    def maximumSum(self, arr: List[int]):
        s = arr[0]
        non = arr[0]
        mx = arr[0]

        for i in arr[1:]:
            if s < 0:
                s = 0
            if i >= 0:
                s = s + i
            else:
                if s + i > non:
                    s = s + i
                else:
                    s = non
            if non < 0:
                non = 0
            non += i
            mx = max(mx, non, s)
        return mx