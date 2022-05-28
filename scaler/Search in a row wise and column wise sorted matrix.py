class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        row, col = 0, len(A[0]) - 1
        while (row < len(A) and col >= 0):
            if A[row][col] < B:
                row += 1
            elif A[row][col] > B:
                col -= 1
            else:
                if col != 0 and A[row][col - 1] == B:
                    col -= 1
                else:
                    return (row + 1)*1009 + col + 1
        return -1

# alternate approach

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = float('inf')
        update = False
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == B:
                    ans = min(ans, ((row + 1) * 1009) + col + 1)
                    update = True
        if update:
            return ans
        return -1


