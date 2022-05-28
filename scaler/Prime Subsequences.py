class Solution:
    # @param A : list of integers
    # @return an integer
    def fastPow(self, base, power, mod):
        if power == 0:
            return 1
        val = self.fastPow(base, power >> 1, mod)
        if power & 1:
            val = (base * val * val) % mod
        else:
            val = (val * val) % mod
        return val % mod

    def solve(self, A):
        # sieve prime bool
        sieve = [True] * (max(A) + 1)
        sieve[0], sieve[1] = False, False
        prime = set()
        i = 2
        while i <= max(A):
            if sieve[i]:
                prime.add(i)
                j = i * i
                while j <= max(A):
                    sieve[j] = False
                    j += i
            i += 1

        power = 0
        for a in A:
            if a in prime:
                power += 1

        mod = 1000000009
        return self.fastPow(2, power, mod) - 1

# alternate approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def fastPow(self, base, power, mod):
        if power == 0:
            return 1
        val = self.fastPow(base, power >> 1, mod)
        if power & 1:
            val = (base * val * val) % mod
        else:
            val = (val * val) % mod
        return val

    def isPrime(self, N):
        if N == 1:
            return False
        i = 2
        while i * i <= N:
            if N % i == 0:
                return False
            i += 1
        return True

    def solve(self, A):

        power = 0

        for a in A:
            if self.isPrime(a):
                power += 1

        mod = 1000000007

        ans = self.fastPow(2, power, mod)
        return ans - 1