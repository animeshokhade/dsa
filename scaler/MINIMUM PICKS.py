class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min_odd = 10 ** 9
        max_even = - 10 ** 9
        for i in A:
            if i % 2 == 1:
                min_odd = min(min_odd, i)
            elif i % 2 == 0:
                max_even = max(max_even, i)

        return max_even - min_odd

# alternate approach

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




