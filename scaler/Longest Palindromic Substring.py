class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)

    pal = ''
    for i in range(n):

        # checking for odd palindromes
        l, r = i - 1, i + 1
        while (l >= 0) and (r < n) and (A[l] == A[r]):
            l -= 1
            r += 1

        if r - l - 1 > len(pal):
            pal = A[l + 1:r]
        elif r - l - 1 == len(pal):
            if A.index(pal[0]) > l:
                pal = A[l + 1:r]

    for i in range(n):

        # checking for even palindromes
        l, r = i - 1, i
        while (l >= 0) and (r < n) and (A[l] == A[r]):
            l -= 1
            r += 1

        if r - l - 1 > len(pal):
            pal = A[l + 1:r]
        elif r - l - 1 == len(pal):
            if A.index(pal[0]) > l:
                pal = A[l + 1:r]

    return pal

