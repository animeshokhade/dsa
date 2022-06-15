class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        start, end = 0, 0
        summ = 0

        while end < n and start <= end:
            if summ == B:
                return A[start:end]

            elif summ < B:
                summ += A[end]
                end += 1

            elif summ > B:
                summ -= A[start]
                start += 1

        if end == n:
            while summ > B:
                summ -= A[start]
                start += 1
            if summ == B:
                return A[start:end]

        return [-1]


# alternative approach

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        start, end = 0, 0
        summ = 0
        for end in range(n):
            summ += A[end]

            while (summ > B) and (start <= end):
                summ -= A[start]
                start += 1
            if summ == B:
                return A[start:end + 1]

        return [-1]


# clean

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        l, r = 0, 0
        sub_sum = 0
        while r < n and l < n:
            if sub_sum < B:
                sub_sum += A[r]
                r += 1
            if sub_sum > B:
                sub_sum -= A[l]
                l += 1
            if sub_sum == B:
                return A[l:r]

        return [-1]

        # TC: O(N); SC: O(1)
