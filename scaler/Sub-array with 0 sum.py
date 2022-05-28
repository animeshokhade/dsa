class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        PS = set()
        summ = 0
        for num in A:
            summ += num
            if (summ in PS) or (summ == 0):
                return 1
            else:
                PS.add(summ)
        return 0

# alternative approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        PS = set()
        summ = 0
        for num in A:
            summ += num
            if summ in PS:
                return 1
            else:
                PS.add(summ)
        if 0 in PS:
            return 1
        return 0

