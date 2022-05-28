class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for index, number in enumerate(A):
            if number <= B:
                count += 1

        if count == 0:
            return 0

        temp = 0
        for index in range(count):
            if A[index] > B:
                temp += 1

        minSwap = temp
        for index in range(count, len(A)):
            if A[index - count] > B:
                temp -= 1
            if A[index] > B:
                temp += 1
            minSwap = min(minSwap, temp)

        return minSwap

# alternate approach

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for index, number in enumerate(A):
            if number <= B:
                count += 1

        if count == 0:
            return 0

        window = A[:count]
        temp = 0
        for index, number in enumerate(window):
            if number > B:
                temp += 1

        minSwap = temp
        for index in range(count, len(A)):
            if window[0] > B:
                temp -= 1
            window.pop(0)
            window += A[index:index + 1]
            if window[-1] > B:
                temp += 1
            minSwap = min(minSwap, temp)

        return minSwap

