class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        current = A.find('bob')
        count = 0

        while current != -1:
            count += 1
            index = current
            current = A.find('bob', index + 1)

        return count

# alternative approach
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        for i in range(n - 2):
            if (A[i:i + 3]) == 'bob':
                count += 1
        return count

# alternative approach
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        for i in range(n - 2):
            if (A[i] + A[i + 1] + A[i + 2]) == 'bob':
                count += 1
        return count


