class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # pascal's triangle
        B = min(B, A-B) #  nCr == nCn-r
        pascal = [0]*(B+1)
        pascal[0] = 1
        for i in range(1, A+1):
            for j in range(min(B, i), 0, -1):
                pascal[j] += pascal[j-1]
                pascal[j] %= C
        return pascal[B] % C

'''
This reduces Space Complexity from O(N * R) to O(R). 
TC: O(N * R) 
'''

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # pascal's triangle
        B = min(B, A-B)
        pascal = [0]*(B+1)
        pascal[0] = 1
        for i in range(1, A+1):
            for j in range(min(i, B), 0, -1):
                if i == j or j == 0:
                    pascal[j] = 1
                else:
                    pascal[j] += pascal[j-1]
                    pascal[j] %= C
        return pascal[B] % C

# alternate approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        combination = [[0] * (B + 1) for _ in range(A + 1)]

        # forming the combination matrix
        for r in range(A + 1):
            for c in range(B + 1):
                if c == r or c == 0:
                    combination[r][c] = 1
                else:
                    combination[r][c] = combination[r - 1][c] + combination[r - 1][c - 1] % C

        return combination[A][B] % C