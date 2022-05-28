class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        summ = 10 ** 10
        flagL = flagR = False
        for j in range(len(A)):
            l = j - 1
            tempL = 10 ** 10
            while l >= 0:
                if A[l] < A[j]:
                    tempL = min(tempL, B[l])
                    flagL = True
                l -= 1
            r = j + 1
            tempR = 10 ** 10
            while r < len(A):
                if A[r] > A[j]:
                    tempR = min(tempR, B[r])
                    flagR = True
                r += 1
            summ = min(summ, B[j] + tempL + tempR)

        if (flagL == flagR) and (summ != 10 ** 10):
            return summ
        return -1

