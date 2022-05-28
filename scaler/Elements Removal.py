class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        B = A[::-1]
        ans = 0
        for i in range(len(B)):
            ans += (i + 1) * B[i]

        return ans

# alternative approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        B = A[::-1]
        summ = sum(B)
        cost = summ
        for i in range(len(B)):
            if i != 0:
                cost += summ
            summ -= B[0]
            B = B[1:]
        return cost

# alternative approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        B = A[::-1]
        cost = 0
        for i in range(len(B)):
            cost += sum(B)
            B = B[1:]

        return cost
