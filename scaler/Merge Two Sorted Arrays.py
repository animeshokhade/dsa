class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        lenA, lenB = len(A), len(B)
        indA, indB = 0, 0
        merged = [0] * (lenA + lenB)
        filler = 0 #  this will be used to fill the answer array

        while indA < lenA and indB < lenB:
            if A[indA] < B[indB]:
                merged[filler] = A[indA]
                indA += 1
                filler += 1
            else:
                merged[filler] = B[indB]
                indB += 1
                filler += 1

        # if A is non-empty
        while indA < lenA:
            merged[filler] = A[indA]
            indA += 1
            filler += 1

        # if B is non-empty
        while indB < lenB:
            merged[filler] = B[indB]
            indB += 1
            filler += 1

        return merged

'''
If we merge the two arrays beforehand and then sort, 
TC: O(M + N)(log(M + N))
The above algorithm optimises the solution to - 
TC: O(M + N)
'''
