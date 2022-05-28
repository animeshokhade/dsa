class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        evenSum, oddSum = [], []
        iterations = len(A)
        tempEven = tempOdd = 0
        for index in range(iterations):
            if index % 2 == 0:
                tempEven += A[index]
                evenSum.append(tempEven)
                oddSum.append(tempOdd)
            elif index % 2 != 0:
                tempOdd += A[index]
                evenSum.append(tempEven)
                oddSum.append(tempOdd)

        E = O = count = 0
        for index in range(iterations):
            E = evenSum[index - 1] + oddSum[iterations - 1] - oddSum[index]
            O = oddSum[index - 1] + evenSum[iterations - 1] - evenSum[index]
            if E == O:
                count += 1
        return count

