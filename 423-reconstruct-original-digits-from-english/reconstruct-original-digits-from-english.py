class Solution:
    def originalDigits(self, s: str) -> str:
        dict = Counter(s)
        z = dict['z']
        w = dict['w']
        u = dict['u']
        f = dict['f'] - u
        x = dict['x']
        v = dict['v'] - f
        g = dict['g']
        r = dict['r'] - z - u
        o = dict['o'] - z - w - u
        n = int((dict['n'] - v - o) // 2)      
        return '0' * z + '1' * o + '2' * w + '3' * r + '4' * u + '5' * f + '6' * x + '7' * v + '8' * g + '9' * n