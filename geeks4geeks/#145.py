# question --> https://practice.geeksforgeeks.org/problems/three-way-partitioning/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    # Function to partition the array around the range such
    # that array is divided into three parts.
    def threeWayPartition(self, array, a, b):

    # code here
    n = len(array)
    l, m, r = 0, 0, n - 1

    while m <= r:
        if a < array[m] < b:
            m += 1
        elif array[m] < a:
            array[l], array[m] = array[m], array[l]
            l += 1
            m += 1
        else:
            array[r], array[m] = array[m], array[r]
            r -= 1

    # TC: O(N); SC: O(1)