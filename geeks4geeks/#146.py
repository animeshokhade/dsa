# question --> https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#


class Solution:
    # Function to return the position of the first repeating element.
    def firstRepeated(self, arr, n):

        # arr : given array
        # n : size of the array
        lkp = {}
        for ind, ele in enumerate(arr):
            if ele in lkp:
                return lkp.get(ele)
            lkp[ele] = ind
        return -1

    # TC: O(N); SC: O(N)
