class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        a, b = 0, 0
        while a < len(A) and b < len(B):
            if A[a] == B[b]:
                a += 1
                b += 1
            else:
                b += 1
        if a == len(A):
            return 'YES'
        return 'NO'

# alternative approach

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        start = -1
        for char in A:
            temp = B.find(char, start + 1)

            if temp == -1:
                return "NO"
            else:
                start = temp

        return 'YES'
