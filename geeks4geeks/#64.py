class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        # Code here
        max_so_far = A[-1]
        leader_count = [max_so_far]
        for _ in range(N - 2, -1, -1):
            if A[_] >= max_so_far:
                leader_count.append(A[_])
                max_so_far = A[_]
        return leader_count[::-1]

        # TC: O(N); SC: O(N)
