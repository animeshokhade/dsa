def solve(A):
    n = len(A)
    if n == len(set(A)): return 0
    A.sort()

    # mapping the frequency of array elements
    freq = {}
    for ele in A:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    '''
    We traverse the array and look for elements with frequency greater
    than 1. For every such element, we search the dictionary for elements
    which are greater than the current element and have 0 frequency i.e.
    they are not present in the dictionary.

    For each such element found we add the new element - current element to 
    the stepper. 
    '''

    stepper = 0
    for ele in A:
        unique = ele + 1
        while freq[ele] > 1:
            # finding the next unique element
            if unique not in freq:
                freq[unique] = 1
                freq[ele] -= 1
                stepper += unique - ele
            unique += 1

    return stepper

    '''
    TC: O(N^2)
    SC: O(N)
    This will give TLE.
    '''


# optimised approach

'''
Sort the array. Now traverse the array. 
Everytime the next element is less than or equal to 
the current element increment stepper and change the next index 
value.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        stepper = 0
        for index, ele in enumerate(A):
            if index != len(A) - 1 and A[index + 1] <= ele:
                diff = ele - A[index + 1] + 1  # best understood by observing a test case
                stepper += diff
                A[index + 1] += diff
        return stepper

        '''
        TC: O(NlogN + N) => O(NlogN)
        SC: O(1)
        '''

# simplified

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        stepper = 0
        for index in range(len(A) - 1):
            if A[index + 1] <= A[index]:
                diff = A[index] - A[index + 1] + 1
                stepper += diff
                A[index + 1] += diff
        return stepper

    '''
    TC: O(NlogN + N) => O(NlogN)
    SC: O(1)
    '''
