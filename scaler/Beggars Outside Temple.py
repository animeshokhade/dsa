class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        beggars = [0] * A
        L, R = 0, 0
        rows = len(B)

        for querry in range(rows):
            L = B[querry][0]
            R = B[querry][1]
            P = B[querry][2]
            beggars[L - 1] += P
            if R != len(beggars):
                beggars[R] -= P

        for index in range(1, len(beggars)):
            beggars[index] += beggars[index - 1]

        return beggars

# alternative approach

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        beggars = [0] * A
        L, R = 0, 0
        rows = len(B)

        for querry in range(rows):
            L = B[querry][0]
            R = B[querry][1]
            P = B[querry][2]
            beggars[L - 1] += P
            if R != len(beggars):
                beggars[R] -= P

        summ = beggars[0]
        ans = []
        for index in range(1, len(beggars) + 1):
            ans.append(summ)
            if index == len(beggars):
                break
            summ += beggars[index]

        return ans

