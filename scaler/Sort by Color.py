class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        start, mid = 0, 0
        end = len(A) - 1

        while mid <= end:
            if A[mid] == 1:
                mid += 1
            elif A[mid] == 0:
                A[start], A[mid] = A[mid], A[start]
                start += 1
                mid += 1
            elif A[mid] == 2:
                A[mid], A[end] = A[end], A[mid]
                end -= 1

        return A

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        count_zero, count_one, count_two = 0, 0, 0
        for i in A:
            if i == 0:
                count_zero += 1
            elif i == 1:
                count_one += 1
            else:
                count_two += 1
        zero_array = [0] * count_zero
        one_array = [1] * count_one
        two_array = [2] * count_two
        ans = zero_array + one_array + two_array
        return ans