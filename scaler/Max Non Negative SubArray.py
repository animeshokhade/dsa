class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        summ = 0
        ans = 0
        flag = False
        L, R = 0, 0
        update = False
        length = 0

        for index in range(len(A)):
            if A[index] >= 0:
                if not flag:
                    L = index
                    R = index
                    flag = True
                summ += A[index]

                if summ > ans:
                    ans = summ
                    R = index
                    update = True
                    ret = A[L:R + 1]
                    length = R - L + 1

                elif summ == ans:
                    R = index
                    if R - L + 1 > length:
                        update = True
                        length = R - L + 1
                        ret = A[L:R + 1]

            else:
                summ = 0
                flag = False

        if update:
            return ret
        return []

