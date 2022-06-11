# question --> https://practice.geeksforgeeks.org/problems/perfect-arrays4645/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def IsPerfect(self, arr, n):
        # Complete the function
        l, r = 0, n - 1
        if n == 1: return True
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

    # TC: O(N); SC: O(1)
