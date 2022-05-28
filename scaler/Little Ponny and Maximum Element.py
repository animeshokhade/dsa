class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        if B in A:
            for number in A:
                temp = number - B
                if temp > 0:
                    count += 1
            if count != 0:
                return count
        return -1

# alternate approach

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B not in A:
            return -1

        count = 0
        for i in A:
            if i > B:
                count += 1

        return count




