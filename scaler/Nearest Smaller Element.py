class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
		stack = []
		G = []

		for ele in A:
			if not stack:
				G.append(-1)
			else:
				while stack and ele <= stack[-1]:
					stack.pop()
				if not stack:
					G.append(-1)
				else:
					G.append(stack[-1])
			stack.append(ele)

		return G

		# TC: O(N); SC: O(N)

# clean

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
		stack = []
		G = []

		for ele in A:
			while stack and ele <= stack[-1]:
				stack.pop()
			if not stack:
				G.append(-1)
			else:
				G.append(stack[-1])
			stack.append(ele)

		return G

		# TC: O(N); SC: O(N)