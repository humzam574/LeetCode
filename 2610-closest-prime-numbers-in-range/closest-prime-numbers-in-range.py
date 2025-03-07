class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sv = [True] * (right + 1)
        #def sieve():
        sv[0] = sv[1] = False

        for n in range(2, int(right**0.5) + 1):
            if sv[n]:
                for m in range(n*n, right + 1, n):
                    sv[m] = False
        
        primes = [num for num in range(left, right + 1) if sv[num]]

        if len(primes) < 2:
            return [-1, -1]
        
        diff = inf
        pair = [-1, -1]

        for i in range(1, len(primes)):
            temp = primes[i] - primes[i - 1]
            if temp < diff:
                diff = temp
                pair = [primes[i-1], primes[i]]
        return pair
