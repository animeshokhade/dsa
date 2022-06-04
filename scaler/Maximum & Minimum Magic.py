class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        n = len(A)
        mod = pow(10, 9) + 7

        # max magic number
        '''
        Sort the array, and then take the first half 
        as the first subset and the second half as 
        the second subset. 
        '''

        max_magic = 0
        left = 0
        right = n // 2
        while right < n:
            max_magic += (A[right] - A[left])
            max_magic %= mod
            left += 1
            right += 1

        # min magic number
        '''
        Sort the array, and then traverse the sorted 
        array with two pointers. Subtract adjacent elements
        and increment both the pointers by 2. This approach 
        became apparent by observing the test cases.  
        '''

        min_magic = 0
        left = 0
        right = 1
        while right < n:
            min_magic += (A[right] - A[left])
            min_magic %= mod
            left += 2
            right += 2

        return [max_magic, min_magic]

        '''
        TC: O(NlogN)
        SC: O(1)
        '''