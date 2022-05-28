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

