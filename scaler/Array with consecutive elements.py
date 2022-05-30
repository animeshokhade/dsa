class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        for index in range(1, len(A) - 1):
            if A[index] == A[index - 1] + 1 and A[index + 1] == A[index] + 1:
                continue
            else:
                return 0
        return 1


'''
TC: O(NlogN + N) => O(NlogN)
SC: O(1)
'''


# optimisation

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        minElement = min(A)
        n = minElement + len(A)
        lookup = set()
        for index, a in enumerate(A):
            A[index] -= minElement
            if A[index] < 0 or A[index] >= n: return 0
            if A[index] in lookup: return 0
            lookup.add(A[index])
        return 1


'''
TC: O(N); SC: O(N) 
'''
