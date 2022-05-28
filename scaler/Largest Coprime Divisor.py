class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return A

    return self.gcd(B, A % B)


def cpFact(self, A, B):
    if A == 1:
        return A

    # if B is less than A then this loop will run only 1 time
    # but if B is greater than A then this loop might run multiple times
    while self.gcd(A, B) != 1:
        A //= self.gcd(A, B)

    return A

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def cpFact(self, A, B):
        if A == 1:
            return A

        while self.gcd(A, B) != 1:
            A //= self.gcd(A, B)

        return A



