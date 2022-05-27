class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        even = []
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            elif i % 2 != 0:
                odd.append(i)
        solution = max(even) - min(odd)
        return solution

