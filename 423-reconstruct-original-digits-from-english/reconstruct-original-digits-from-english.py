class Solution:
    def originalDigits(self, s: str) -> str:
        dict, arr, ans = Counter(s), (('z', 'ero', '0'), ('w', 'to', '2'), ('u', 'for', '4'), ('x', 'si', '6'), ('g', 'eiht', '8'), ('f', 'ive', '5'), ('v', 'seen', '7'), ('i', 'nne', '9'),  ('r', 'thee', '3'), ('o', 'ne', '1')), []
        for i in range(10):
            if arr[i][0] in dict and dict[arr[i][0]] != 0:
                val = dict[arr[i][0]]; ans = ans + [arr[i][2]] * val
                for char in arr[i][1]: dict[char] -= val
        return ''.join(sorted(ans))
