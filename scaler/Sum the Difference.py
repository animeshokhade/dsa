# brute force

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        mod = 1000000007
        n = len(A)
        max_diff = 0

        for left in range(n):
            for right in range(left + 1, n):
                max_diff += (1 << (right - left - 1)) * (A[right] - A[left]) % mod

        return max_diff % mod

        '''
	    TC: O(N^2)
	    SC: O(1)
	    '''


# optimised

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mod = pow(10, 9) + 7
        A = sorted(A)
        maxSum = 0
        for index, number in enumerate(A):
            maxSum += ((1 << index) * number) % mod

        minSum = 0
        for index in range(len(A) - 1, -1, -1):
            minSum += ((1 << (len(A) - 1 - index)) * A[index]) % mod

        return (maxSum - minSum) % mod

# clean

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        mod = 1000000007
        n = len(A)
        max_sum = 0
        min_sum = 0

        for index in range(n):
            # contribution of each element to maximum sum will be for all the subsets in which it is maximum
            max_sum += A[index] * ((1 << index) % mod)

            # contribution of each element to minimum sum will be for all the subsets in which it is minimum
            min_sum += A[index] * ((1 << n - 1 - index) % mod)

        return (max_sum - min_sum) % mod


'''
TC: O(NlogN)
SC: O(1)
'''
