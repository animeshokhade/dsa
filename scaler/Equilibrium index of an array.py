class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        rightSum = sum(A)
        leftSum = 0

        for index in range(len(A)):
            rightSum -= A[index]
            if leftSum == rightSum:
                return index
            leftSum += A[index]

        return -1

# alternate approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        PS = [0] * len(A)
        SS = [0] * len(A)

        PS[0] = A[0]
        SS[0] = A[-1]
        for index in range(1, len(A)):
            PS[index] = A[index] + PS[index - 1]
            SS[index] = A[len(A) - index - 1] + SS[index - 1]

        if SS[-2] == 0:
            return 0

        for index in range(1, len(A) - 1):
            # if len(A) - index - 2 < 0:
            #     if PS[index - 1] == 0:
            #         return index

            if PS[index - 1] == SS[len(A) - index - 2]:
                return index

        if PS[-2] == 0:
            return len(A) - 1

        return -1

# alternate approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        PS = [0] * len(A)
        SS = [0] * len(A)

        PS[0] = A[0]
        SS[0] = A[-1]
        for index in range(1, len(A)):
            PS[index] = A[index] + PS[index - 1]
            SS[index] = A[len(A) - index - 1] + SS[index - 1]

        # print(PS, SS)
        if SS[-2] == 0:
            return 0

        for index in range(1, len(A)):
            if len(A) - index - 2 < 0:
                if PS[index - 1] == 0:
                    return index

            elif PS[index - 1] == SS[len(A) - index - 2]:
                return index

        return -1