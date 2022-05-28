class Solution:
    # @param A : list of integers
    # @return an integer
    def GCD(self, a, b):
        if b == 0:
            return a
        return self.GCD(b, a % b)

    def solve(self, A):
        # prefix GCD
        p = [0] * len(A)

        # suffix GCD
        s = [0] * len(A)

        # filling up prefixGCD
        gcd = 0
        for i in range(1, len(A)):
            gcd = self.GCD(gcd, A[i - 1])
            p[i] = gcd

        # filling up suffixGCD
        gcd = 0
        for j in range(len(A) - 2, -1, -1):
            gcd = self.GCD(gcd, A[j + 1])
            s[j] = gcd

            # cal max GCD
        maxGCD = float('-inf')
        for index, element in enumerate(A):
            delNum = self.GCD(p[index], s[index])
            maxGCD = max(maxGCD, delNum)

        return maxGCD

# alternate approach

