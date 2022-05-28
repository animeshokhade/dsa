class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for i in A:
            if not i.isalpha():
                return 0
        return 1

# alternative approach

class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for i in A:
            if not ((65 <= ord(i) <= 90) | (97 <= ord(i) <= 122)):
                return 0
        return 1

