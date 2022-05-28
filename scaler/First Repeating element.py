class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        tracker = set()
        n = len(A)
        index = -1
        for i in range(n - 1, -1, -1):
            if A[i] in tracker:
                index = i
            else:
                tracker.add(A[i])
        if index == -1:
            return index
        return A[index]

# alternative approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        tracker = dict()
        for num in A:
            if tracker.get(num) != None:
                tracker[num] += 1
            else:
                tracker[num] = 1

        index = 10 ** 9
        for key in tracker:
            if tracker[key] > 1:
                index = min(index, A.index(key))
        if index != 10 ** 9:
            return A[index]
        return -1