class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
        n = len(A)
        left, right = 0, len(A) - 1

        ans = 0

        maxLeft = float('-inf')
        maxRight = float('-inf')

        while left <= right:
            if A[left] <= A[right]:
                if A[left] >= maxLeft:
                    maxLeft = A[left]

                else:
                    ans += maxLeft - A[left]
                left += 1
            else:
                if A[right] >= maxRight:
                    maxRight = A[right]
                else:
                    ans += maxRight - A[right]
                right -= 1
        return ans

# alternative approach

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        # leftMax
        leftMax = list()
        temp = float('-inf')
        for a in A:
            if a > temp:
                temp = a
            leftMax.append(temp)

        # rightMax
        rightMax = list()
        temp = float('-inf')
        for a in range(len(A) - 1, -1, -1):
            if A[a] > temp:
                temp = A[a]
            rightMax.append(temp)
        rightMax = rightMax[::-1]

        ans = 0
        if A:
            for i in range(1, len(A) - 1):
                height = min(leftMax[i], rightMax[i]) - A[i]
                if height > 0:
                    ans += height

        return ans

