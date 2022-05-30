class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        n = len(A)
        if n // 2 > B:
            for swap in range(B):
                min_ele = min(A[swap:])
                min_index = A.index(min_ele, swap)
                A[swap], A[min_index] = A[min_index], A[swap]
            return A[B - 1]
        else:
            for swap in range(n - B + 1):
                max_ele = max(A[swap:])
                max_index = A.index(max_ele, swap)
                A[swap], A[max_index] = A[max_index], A[swap]
            return A[n - B]


'''
TC: O(N^2); SC: O(1)
We find kth minimum when k is smaller than n // 2, 
else we find n - k + 1th maximum. 
Optimisation
'''


# selection sort -> clean code
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        for swap in range(B):
            min_ele = min(A[swap:])
            min_index = A.index(min_ele, swap)
            A[swap], A[min_index] = A[min_index], A[swap]
        return A[B - 1]


'''
TC: O(N^2); SC: O(1)
In this question, we can either arrange the selected elements at the 
front or at the back. We'll have to swap accordingly. 
'''


# selection sort

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        for swap in range(B):
            temp = A[swap]
            index = swap
            for i in range(swap + 1, len(A)):
                if A[i] < temp:
                    temp = A[i]
                    index = i
            if index != swap:
                A[swap], A[index] = A[index], A[swap]
        return A[B - 1]


'''
TC: O(N^2); SC: O(1)
'''


# standard sort

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        A.sort()
        return A[B - 1]


# TC: O(NlogN); SC: O(1)

# bubble sort


'''
Preferred approach => Selection sort
'''
