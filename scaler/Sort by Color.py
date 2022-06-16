# Two Pointer approach
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

    # TC: O(N); SC: O(1)

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        n = len(A)
        count_zero, count_one, count_two = 0, 0, 0
        for i in A:
            if i == 0:
                count_zero += 1
            elif i == 1:
                count_one += 1
            else:
                count_two += 1
        for ind in range(n):
            if count_zero != 0:
                A[ind] = 0
                count_zero -= 1
            elif count_one != 0:
                A[ind] = 1
                count_one -= 1
            else:
                A[ind] = 2
                count_two -= 1

        return A

    # TC: O(N); SC: O(1)