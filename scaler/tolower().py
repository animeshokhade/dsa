class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        A = [x.lower() for x in A]
        return A

# alternative approach

class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        A = ' '.join(A)
        A = A.lower()
        A = A.split()

        return A
