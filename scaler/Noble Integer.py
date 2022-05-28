class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A = sorted(A, reverse = True)
        if A[0] == 0:
            return 1
        for i in range(len(A)):
            if i:
                if A[i] != A[i - 1]:
                    if A[i] == i:
                        return 1
        return -1

