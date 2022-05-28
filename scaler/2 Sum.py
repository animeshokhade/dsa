class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
		hashh = dict()
		n = len(A)
		for i in range(n):
			if A[i] in hashh:
				return [hashh[A[i]] + 1, i + 1]
			elif B - A[i] not in hashh:
				hashh[B - A[i]] = i

		return []
