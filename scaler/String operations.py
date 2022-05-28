class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A * 2
        A = list(A)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for index, char in enumerate(A):
            if char.isupper():
                A[index] = ''
            elif char in vowels:
                A[index] = '#'

        return ''.join(A)


