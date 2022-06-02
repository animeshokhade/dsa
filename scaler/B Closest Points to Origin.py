import functools


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def compare(self, a, b):
        dis_A = a[0] * a[0] + a[1] * a[1]
        dis_B = b[0] * b[0] + b[1] * b[1]
        if dis_A <= dis_B:
            return -1
        else:
            return 1

    def solve(self, A, B):
        A.sort(key=functools.cmp_to_key(self.compare))
        return A[:B]

    '''
    TC: O(NlogN)
    SC: O(1) 
    '''

# One liner

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        return sorted(A, key=lambda x: x[0] * x[0] + x[1] * x[1])[:B]

    '''
    TC: O(NlogN)
    SC: O(1) 
    '''
