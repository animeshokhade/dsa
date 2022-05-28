class Solution:
	# @param A : string
	# @return an integer
    def factorial(self, A):
        if A == 0: return 1
        return A * self.factorial(A - 1)

	def findRank(self, A):
        ans = 0
        n = len(A)
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    count += 1
            ans += (count * self.factorial(n - 1 - i)) % 1000003

        return (ans + 1) % 1000003
        # +1 is to count the string of interest
'''
Optimised
TC: O(N^2)
SC: O(1)
'''

# alternate approach

class Solution:
    # @param A : string
    # @return an integer
    def factorial(self, A):
        if A == 0: return 1
        return A * self.factorial(A - 1)

    def findRank(self, A):
        smallSuffix = [0] * len(A)
        ans = 0
        n = len(A)
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    count += 1
            smallSuffix[i] = count
        for s in range(n):
            ans += (smallSuffix[s] * self.factorial(n - 1 - s)) % 1000003
        return (ans + 1) % 1000003
        # +1 is to count the string of interest
'''
TC: O(N^2)
SC: O(N)
'''

# alternate approach

class Solution:
    # @param A : string
    # @return an integer
    def factorial(self, A):
        if A == 0: return 1
        return A * self.factorial(A - 1)

    def findRank(self, A):
        smallSuffix = [0] * len(A)
        ans = 0
        n = len(A)
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    count += 1
            smallSuffix[i] = count
        for s in range(n):
            ans += (smallSuffix[s] * self.factorial(n - 1 - s)) % 1000003
        return (ans + 1) % 1000003

