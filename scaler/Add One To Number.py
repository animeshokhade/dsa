class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        slicer = 0
        for index, number in enumerate(A):
            if number != 0:
                break
            slicer = index + 1

        if slicer != 0:
            A = A[slicer:]

        carry = 1
        summ = 0
        for index in range(len(A) - 1, -1, -1):
            summ = A[index] + carry
            carry = summ // 10
            A[index] = summ % 10

        if carry >= 1:
            A = [carry] + A

        return A

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A = [str(x) for x in A]
        A = int(''.join(A))
        A += 1
        A = list(str(A))
        return A