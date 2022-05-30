class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        distinct = -2
        allEqual = True
        for index in range(len(A) - 2, -1, -1):
            if A[index] != A[index + 1]:
                distinct = index
                allEqual = False
                break
        if allEqual: return 0
        return A[distinct]


'''
TC: O(NlogN)
SC: O(1) 
'''


# optimised approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxx = max(A)
        second_max = 0
        for index in range(len(A)):
            if A[index] != maxx:
                second_max = max(second_max, A[index])
        return second_max


'''
TC: O(N)
SC: O(1)
'''
