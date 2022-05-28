class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        vowel = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        x = 0
        for index, char in enumerate(A):
            if char in vowel:
                x += n - index
        return x % 10003

# alternate approach

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if B == 0:
            ans = [index for index, a in enumerate(A)]
            return ans

        n = len(A)
        countLeft, countRight = [0] * n, [0] * n

        tempCount = 0

        for i in range(1, n):
            if A[i] != A[i - 1]:
                tempCount += 1
                countLeft[i] = tempCount
            else:
                countLeft[i] = 0
                tempCount = 0

        tempCount = 0

        for j in range(n - 2, -1, -1):
            if A[j] != A[j + 1]:
                tempCount += 1
                countRight[j] = tempCount
            else:
                countRight[j] = 0
                tempCount = 0

        ans = []

        for index, ele in enumerate(A):
            if countLeft[index] >= B and countRight[index] >= B:
                ans.append(index)

        return ans


