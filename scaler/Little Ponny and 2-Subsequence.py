class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        small = min(A[:len(A) - 1])
        subSmall = min(A[A.index(small) + 1:])

        return small + subSmall

# alternative approach

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        small, subSmall = min(A), 'z'

        smallIndex = A.index(small)

        if smallIndex != len(A) - 1:
            subSmall = min(A[smallIndex + 1:])

        else:
            subSmall = small
            small = min(A[:len(A) - 1])

        return small + subSmall
