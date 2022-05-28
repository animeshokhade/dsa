class Solution:
	# @param A : tuple of integers
	# @return an integer
	def hammingDistance(self, A):
        i = 32
        ans = 0

        while i >= 0:
            setBit = 0
            for a in A:
                if a >> i & 1:
                    setBit += 1
            ans += 2 * setBit * (len(A) - setBit)
            i -= 1

        return ans % 1000000007

