class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        min_sum = float('inf')
        for a in range(n - 2):
            b, c = a + 1, n - 1
            while b < c:
                cur_sum = A[a] + A[b] + A[c]
                if cur_sum == B:
                    return cur_sum
                if abs(min_sum - B) > abs(cur_sum - B):
                    min_sum = cur_sum
                if cur_sum > B:
                    c -= 1
                else:
                    b += 1
        return min_sum

        # TC: O(N^2); SC: O(1)