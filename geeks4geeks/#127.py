# question --> https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1/?page=1#

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        # code here
        ret = []

        for i in range(0, N, K):
            if i >= N - K:
                l, r = i, N - 1
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
                break
            l, r = i, i + K - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

    # TC: O(N); SC: O(N)
