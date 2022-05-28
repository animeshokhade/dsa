class Solution:
    # @param A : string
    # @return an integer

    def factorial(self, A, mod):
        fact = [1]
        for i in range(1, A + 1):
            fact.append((fact[-1] * i) % mod)
        return fact

    def power(self, base, power, mod):
        if power == 0: return 1
        ans = self.power(base, power >> 1, mod)
        if power & 1:
            return (ans * ans * base) % mod
        return (ans * ans) % mod

    def inverse_num(self, A, mod):
        return self.power(A, mod - 2, mod)

    def findRank(self, A):
        mod = 1000003
        n = len(A)
        c = {}
        for C in A:
            if C in c:
                c[C] += 1
            else:
                c[C] = 1
        fact = self.factorial(n, mod)
        ans = 1
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    count += 1
            numerator = fact[n - i - 1]
            denominator = 1
            for k in c:
                denominator *= fact[c[k]]
            denominator = self.inverse_num(denominator, mod)
            ans += count * numerator * denominator
            ans %= mod
            c[A[i]] -= 1  # updating the duplicate count
        return ans

# alternative approach

import collections

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        # find the lexicographic rank of the string
        mod = 1000003
        n = len(A)
        c = collections.Counter(A)
        fact = self.factorial(n, mod)
        res = 1
        for i in range(n):
            rank = 0
            for j in range(i+1, n):
                if A[i] > A[j]:
                    rank += 1
            num = fact[n-i-1]%mod
            den = 1
            for k in c:
                den *= fact[c[k]] % mod
            den = self.inverse_num(den, mod)
            res = (res + rank*num*den)%mod
            c[A[i]] -= 1
        return res

    def inverse_num(self, n, mod):
        return pow(n, mod-2, mod)

    def factorial(self, n, mod):
        fact = [1]
        for i in range(1, n+1):
            fact.append(fact[-1]*i%mod)
        return fact

