class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        summ = 0
        for index in range(B):
            summ += A[index]

        ans = summ
        for index in range(B):
            ans = max(ans, summ - A[B - index - 1] + A[- index - 1])
            summ = summ - A[B - index - 1] + A[- index - 1]

        return ans

# alternate approach

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        PS = [0 for _ in range(len(A))]
        SS = [0 for _ in range(len(A))]

        PS[0] = A[0]
        SS[0] = A[-1]

        for index in range(1, len(A)):
            PS[index] += A[index] + PS[index - 1]
            SS[index] += A[len(A) - index - 1] + SS[index - 1]

        ans = max(PS[B - 1], SS[B - 1])

        for index in range(B - 1):
            ans = max(ans, PS[B - 2 - index] + SS[index])

        return ans

