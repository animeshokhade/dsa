class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        import sys

        n = len(A)
        count1, count2 = 0, 0
        first = sys.maxsize
        second = sys.maxsize

        for i in range(n):
            if first == A[i]:
                count1 += 1

            elif second == A[i]:
                count2 += 1

            elif count1 == 0:
                count1 += 1
                first = A[i]

            elif count2 == 0:
                count2 += 1
                second = A[i]

            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for i in range(n):
            if A[i] == first:
                count1 += 1

            elif A[i] == second:
                count2 += 1

        if count1 > n // 3:
            return first

        elif count2 > n // 3:
            return second

        return -1


