class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0: return 0
        if B == 0: return 1
        power = self.pow(A, B >> 1, C) % C
        if B & 1:
            return power * power * A % C
        else:
            return power * power % C

# alternative approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B == 0:
            if A != 0:
                return 1
        if A == 0 and B == 0:
            return 0
        ret = pow(A, B // 2, C) % C
        if B & 1 == 0:
            return (ret % C * ret % C) % C
        else:
            return ((((A % C) * (ret % C)) % C) * (ret % C)) % C

# alternative approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B == 0:
            if A != 0:
                return 1
            else:
                return 0
        ret = pow(A, B // 2, C) % C
        if B & 1 == 0:
            return (ret % C * ret % C) % C
        else:
            return ((((A % C) * (ret % C)) % C) * (ret % C)) % C

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B % 2 == 0:
            return pow(A, B // 2, C) * pow(A, B // 2, C) % C
        else:
            return A * pow(A, B // 2, C) * pow(A, B // 2, C) % C
