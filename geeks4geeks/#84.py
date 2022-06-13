# question --> https://practice.geeksforgeeks.org/problems/multiply-matrices/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

def multiply(A, B, C, n):
    # Code here
    for r in range(n):
        for c in range(n):
            for a in range(n):
                C[r][c] += A[r][a] * B[a][c]
    return
    # TC: O(N^3); SC: O(1)
