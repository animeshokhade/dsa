# question --> https://practice.geeksforgeeks.org/problems/toeplitz-matrix/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

def isToepliz(lis, n, m):
    # code here
    for r in range(n - 1):
        for c in range(m - 1):
            if lis[r][c] != lis[r + 1][c + 1]:
                return 0
    return 1

    # TC: O(N^2); SC: O(1)
