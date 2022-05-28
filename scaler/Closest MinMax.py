class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = float('inf')
        maxx, minn = max(A), min(A)
        latestMax = latestMin = -1
        for index, number in enumerate(A):
            if number == maxx:
                if latestMin != -1:
                    ans = min(ans, index - latestMin + 1)
                latestMax = index
            elif number == minn:
                if latestMax != -1:
                    ans = min(ans, index - latestMax + 1)
                latestMin = index
        if ans == float('inf'):
            return 1
        return ans
