class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def power(self, base, power, mod):
        if power == 0: return 1
        ans = self.power(base, power >> 1, mod)
        if power & 1:
            return (ans * ans * base) % mod
        return (ans * ans) % mod

    def solve(self, A, B, C):
        if A == 1 and B == 1 and C == 1: return 0
        B = min(A - B, B)
        numerator, denominator = 1, 1
        for i in range(B):
            numerator *= A - i
            numerator %= C
            denominator *= i + 1
            denominator %= C

        # this expression is derived using Little Fermat's Theorem
        return (numerator * self.power(denominator, C - 2, C)) % C

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def power(self, base, power, mod):
        if power == 0: return 1
        ans = self.power(base, power >> 1, mod)
        if power & 1:
            return (ans * ans * base) % mod
        return (ans * ans) % mod

    def solve(self, A, B, C):
        if C == 1:
            return 0
        if A == 1:
            return 1
        mx = max(A - B, B)
        mn = min(A - B, B)
        numerator, denominator = 1, 1
        for n in range(mx + 1, A + 1):
            numerator *= n
            numerator %= C
        for d in range(2, mn + 1):
            denominator *= d
            denominator %= C
        return (numerator * self.power(denominator, C - 2, C)) % C

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if C == 1:
            return 0
        if A == 1:
            return 1
        mx = max(A - B, B)
        mn = min(A - B, B)
        denominator = 1
        numerator = 1
        for n in range(mx + 1, A + 1):
            numerator *= n
            if numerator >= C:
                numerator %= C
        for d in range(2, mn + 1):
            denominator *= d
            if denominator >= C:
                denominator %= C
        return (numerator * pow(denominator, C - 2, C)) % C

# alternate approach

import sys
sys.setrecursionlimit(1000000)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B < 0:
            return A
        if B == 0:
            return 1 if A != 0 else 0
        else:
            if B % 2 == 0:
                return self.pow((A*A)%C, B//2, C) % C
            else:
                return (A * self.pow((A*A)%C, (B-1)//2, C) % C)%C

    def solve(self, A, B, C):
        B = min(B, A-B)
        numerator = 1
        denominator = 1
        for i in range(B):
            numerator = (numerator * (A-i)) % C
            denominator = (denominator * (i+1)) % C
        return (numerator % C * self.pow(denominator, C-2, C) % C) % C
