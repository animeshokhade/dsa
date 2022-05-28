class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def LCM(self, A, B):
        product = A * B
        iterations = min(A, B)
        for i in range(1, iterations + 1):
            if (A % i == 0) and (B % i == 0):
                HCF = i

        LCM = product // HCF
        return LCM

