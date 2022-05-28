class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        diff = 10 ** 9
        tracker = dict()
        for index, num in enumerate(A):
            if num in tracker:
                diff = min(diff, abs(index - tracker[num]))
            else:
                tracker[num] = index
        if diff != 10 ** 9:
            return diff
        return -1

