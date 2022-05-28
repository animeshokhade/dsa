class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def power(self, A, power, mod):
        # Base Case
        if power == 0:
            return 1

        # Recursive relation
        rec = self.power(A, power >> 1, mod) % mod

        if power & 1:
            return A * rec * rec % mod
        return rec * rec % mod

    def solve(self, A, B):
        return self.power(A, B - 2, B)

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        '''
        Time Complexity: O(log B)
        Using Fermat's Theorem: A ^ -1 % B = A ^ (B - 2) % B
        '''

        def fast_pow(a, p, m):
            # base case
            if p == 0:
                return 1
            if a == 0:
                return 0
            # for handling -ve values
            if p == 1 and a < 0:
                return a + p

            # when p is even
            if p & 1 == 0:
                return fast_pow(a * a % m, p // 2, m)
            else:
                return a * fast_pow(a * a % m, (p - 1) // 2, m) % m

        return fast_pow(a=A, p=B - 2, m=B)
