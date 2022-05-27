# question --> https://practice.geeksforgeeks.org/problems/count-of-smaller-elements5947/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

def countOfElements( a, n, x):
    ans = 0
    for index in range(n):
        if a[index] <= x:
            ans += 1
    return ans

    # TC: O(N); SC: O(1)
# end 