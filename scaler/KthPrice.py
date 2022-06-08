class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def check(self, A, B):
        count = 0
        for _ in A:
            if _ <= B:
                count += 1
        return count

    def solve(self, A, B):
        low = min(A)
        high = max(A)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            count = self.check(A, mid)
            if count >= B:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    # TC: O((max - min)log(max - min)); SC: O(1)
