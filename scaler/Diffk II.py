class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        set_A = set()
        for num in A:
            if ((num - B) in set_A) or ((num + B) in set_A):
                return 1
            else:
                set_A.add(num)
        return 0




