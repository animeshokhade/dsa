# question --> https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1/?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr, n):
        # code here
        arr.sort()
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                summ = arr[l] + arr[r] + arr[i]
                if arr[l] + arr[r] + arr[i] == 0:
                    return 1
                elif summ > 0:
                    r -= 1
                else:
                    l += 1

        return 0

    # TC: O(N^2); SC: O(1)