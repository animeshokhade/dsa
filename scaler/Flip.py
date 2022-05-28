class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        summ, maxx = 0, 0
        L, R = 0, 0

        ans = [L, R]

        for index in range(len(A)):
            if A[index] == '1':
                summ -= 1
            else:
                summ += 1

            if summ > maxx:
                maxx = summ
                ans = [L + 1, R + 1]

            if summ < 0:
                L = index + 1
                R = index + 1
                summ = 0

            else:
                R += 1

        if maxx:
            return ans
        return []

# alternate approach

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A = list(A)
        for index in range(len(A)):
            if A[index] == '0':
                A[index] = 1
            elif A[index] == '1':
                A[index] = -1

        L, R = 0, 0
        summ, ans = 0, 0
        ret = []
        flag = False
        update = False

        for index in range(len(A)):
            summ += A[index]
            if summ >= 0:
                if not flag:
                    L = index + 1
                    R = index + 1
                    flag = True
                if summ > ans:
                    ans = summ
                    R = index + 1
                    update = True
                    ret = [L, R]
            else:
                flag = False
                summ = 0

        if update:
            return ret
        return []

