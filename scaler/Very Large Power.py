class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def factorial(self, B, mod):
        ret = 1
        for f in range(2, B + 1):
            ret = (ret * f) % mod
        return ret

    def power(self, A, B, mod):
        if B == 0:
            return 1
        res = self.power(A, B >> 1, mod)
        if B & 1:
            return (A * res * res) % mod
        return (res * res) % mod

    def solve(self, A, B):
        mod = 1000000007
        fac = self.factorial(B, mod - 1)
        # we take mod - 1 because (mod - 1) power will decompose to 0
        return self.power(A, fac, mod)

'''
As per Fermat Little Theorem, a^(p - 1) % p if p is prime = 1. 
So, to calculate A^B!, we can decompose B! into (p - 1) * (p - 1)... * (b)
Now, as per the theorem, A ^ (p - 1) % p is 1, so in order to do that we take
B! mod with (p - 1) which eliminates all instances of p - 1 which are embedded 
inside the val of B!. And thus we only calculate A^b which substantially reduces
runtime. 
'''

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def factorial(self, B, mod):
        ret = 1
        for f in range(2, B + 1):
            ret = (ret * f) % mod
        return ret

    def power(self, A, B, mod):
        if B == 0:
            return 1
        res = self.power(A, B // 2, mod)
        if B & 1:
            return (A * res * res) % mod
        return (res * res) % mod

    def solve(self, A, B):
        mod = 1000000007
        fac = self.factorial(B, mod - 1)
        return self.power(A, fac, mod)

