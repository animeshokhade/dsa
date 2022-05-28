class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        tracker = set()
        count = 0

        for num in A:
            if num ^ B in tracker:
                count += 1
            tracker.add(num)

        return count

# alternative approach

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        tracker = set()
        numbers = set(A)
        count = 0

        for num in numbers:
            if (num ^ B in numbers) and (num ^ B not in tracker):
                count += 1
            tracker.add(num)

        return count